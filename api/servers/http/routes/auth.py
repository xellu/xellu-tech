from ..router import v2auth, Sessions, Limiter
from ..services.adapter import Reply, Require

from core.tools import RandomStr, HashStr
from core.templates.UserTemplate import UserTemplate, SanitizeUser
from core import Database, Config

from flask import request
import time
import re

@v2auth.route("/register", methods=["POST"])
@Limiter.limit("5/minute")
def register():
    data = Require(request,
        invite=str,
        username=str,
        password=str,     
    ).body()
    
    if not data.ok:
        return Reply(**data.content), 400
    
    data.content["username"] = data.content["username"].lower()
    if Database.get_database("xelapi").users.find_one({"username": data.content["username"]}):
        return Reply(error="Username already in use"), 400

    if not Database.get_database("xelapi").invites.find_one({"code": data.content["invite"]}):
        return Reply(error="Invalid invite code"), 400

    #validate username
    if len(data.content["username"]) < 3:
        return Reply(error="Username too short"), 400
    
    if len(data.content["username"]) > 32:
        return Reply(error="Username too long"), 400
    
    if not re.match(r"^[a-z0-9_]+$", data.content["username"]):
        return Reply(error="Username contains invalid characters"), 400
    
    #validate password
    if len(data.content["password"]) < 8:
        return Reply(error="Password too short"), 400
    
    user = UserTemplate()
    user["username"] = data.content["username"]
    user["password"] = HashStr(f"{user['_id']}${data.content['password']}")

    Database.get_database("xelapi").users.insert_one(user)
    Database.get_database("xelapi").invites.delete_one({"code": data.content["invite"]})
    
    session = Sessions.create(
        user_id = user["_id"],
        expire = Config.get("AUTH.EXPIRE") + time.time(),
        scopes = ["*"]
    )
    
    r = Reply(session=session)
    r.set_cookie("session", value=session)
    return r, 200

@v2auth.route("/login", methods=["POST"])
@Limiter.limit("10/minute")
def login():
    data = Require(request,
        username=str,
        password=str,     
    ).body()
    
    if not data.ok:
        return Reply(**data.content), 400
    
    user = Database.get_database("xelapi").users.find_one({"username": data.content["username"].lower()})
    if not user:
        return Reply(error="User not found"), 404
    
    if user["password"] != HashStr(f"{user['_id']}${data.content['password']}"):
        return Reply(error="User not found"), 404
    
    session = Sessions.create(
        user_id = user["_id"],
        expire = Config.get("AUTH.EXPIRE") + time.time(),
        scopes = ["*"]
    )
    
    r = Reply(session=session)
    r.set_cookie("session", value=session)
    return r, 200

@v2auth.route("/verify", methods=["POST"])
@Sessions.protect()
def verify():
    user = Sessions.get_user(request.cookies.get("session"))
    if not user:
        return Reply(error="Session expired"), 401
    
    return Reply(
        **SanitizeUser(user)
    )
    
@v2auth.route("/logout", methods=["POST"])
@Sessions.protect()
def logout():
    delete_all = Require(
        request,
    
        delete_all=bool,
        password=str
    ).body()
    
    if not delete_all.ok:
        #delete current session
        Sessions.delete(request.cookies.get("session"))

        return Reply(), 200
    
    #delete all sessions
    user = Sessions.get_user(request.cookies.get("session"))
    Sessions.delete_all(user_id=user["_id"])
    return Reply(), 200