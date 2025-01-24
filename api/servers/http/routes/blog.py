from ..router import v2blog, Sessions
from ..services.adapter import Reply, Require

from core import Database

from flask import request

@v2blog.route("/fetch")
def fetch_blogs():
    data = Require(request, entries=int, page=int).query()
    if not data.ok:
        return Reply(**data.content), 400
    
    blogs = Database.get_database("blog").blog.find().skip(data.content["page"] * data.content["entries"]).limit(data.content["entries"])
    
    return Reply(blogs=[blog for blog in blogs]), 200