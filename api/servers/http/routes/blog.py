from ..router import Sessions, Limiter, v2blog
from ..services.adapter import Reply, Require

from core.templates.BlogTemplate import BlogPostTemplate
from core import Database

from flask import request
import time

@v2blog.route("/create", methods=["POST"])
@Limiter.limit("3/minute")
@Sessions.protect()
def create_post():
    user = Sessions.get_user(request.cookies.get("session"))
    if not user.get("admin"):
        return Reply(error="Insufficient permissions"), 403
        
    data = Require(request,
        title = str,
        brief = str,
        content = str
    ).body()
    
    if not data.ok:
        return Reply(**data.content), 400
    
    post = BlogPostTemplate()
    post["title"] = data.content["title"]
    post["brief"] = data.content["brief"]
    post["content"] = data.content["content"]
    post["author"] = user["_id"]
    
    Database.get_database("xelapi").blog.insert_one(post)
    
    return Reply(id=post["_id"]), 200

@v2blog.route("/post/<string:post_id>", methods=["GET", "DELETE", "PATCH"])
@Limiter.limit("6/minute")
def manage_post(post_id):
    post = Database.get_database("xelapi").blog.find_one({"_id": post_id}) 
    if not post:
        return Reply(error="Post not found"), 404
    
    #public access----
    
    #get post content
    if request.method == "GET":
        author = Database.get_database("xelapi").users.find_one({"_id": post["author"]})
        post["author"] = author["username"] if author else "Unknown"
        return Reply(post=post), 200
    
    #restricted access----
    user = Sessions.get_user(request.cookies.get("session"))

    if not user:
        return Reply(error="Unauthorized"), 401 
    if not user["admin"]:
        return Reply(error="Insufficient permissions"), 403
    
    #delete post
    if request.method == "DELETE":
        Database.get_database("xelapi").blog.delete_one({"_id": post_id})
        return Reply(), 200
    
    #edit post
    if request.method == "PATCH":
        data = Require(request,
            title = str,
            brief = str,
            content = str
        ).body()
        
        if not data.ok:
            return Reply(**data.content), 400
        
        post["title"] = data.content["title"]
        post["brief"] = data.content["brief"]
        post["content"] = data.content["content"]
        post["lastModified"] = time.time()
        
        Database.get_database("xelapi").blog.update_one({"_id": post_id}, {"$set": post})
        
        return Reply(), 200
    
@v2blog.route("/posts", methods=["GET"])
@Limiter.limit("15/minute")
def post_list():
    start = int(request.args.get("page", 1)) * 10 - 10
    
    posts = list(Database.get_database("xelapi").blog.find().sort("createdAt", -1).skip(start).limit(10))
    
    for post in posts:
        author = Database.get_database("xelapi").users.find_one({"_id": post["author"]})
        post["author"] = author["username"] if author else "Unknown"
        
    return Reply(posts=posts), 200