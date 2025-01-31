from ..router import v2acc, Sessions, Limiter

from ..services.adapter import Reply, Require
from core.tools import RandomStr, HashStr
from core import Database, Config

from flask import request
import re

@v2acc.route("/username", methods=["POST"])
@Sessions.protect()
@Limiter.limit("3/hour")
def change_username():
    data = Require(request, username=str, password=str).body()
    if not data.ok:
        return Reply(**data.content), 400
    
    data.content["username"] = data.content["username"].lower()
    
    user = Sessions.get_user(request.cookies.get("session"))
    if not HashStr(f"{user['_id']}${data.content['password']}") == user["password"]:
        return Reply(error="Password is incorrect"), 400
    
    if len(data.content["username"]) < 3:
        return Reply(error="Username too short"), 400
    
    if len(data.content["username"]) > 32:
        return Reply(error="Username too long"), 400
    
    if not re.match(r"^[a-z0-9_]+$", data.content["username"]):
        return Reply(error="Username contains invalid characters"), 400
    
    if Database.get_database("xelapi").users.find_one({"username": data.content["username"]}):
        return Reply(error="Username already in use"), 400
    
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {"$set": {"username": data.content["username"]}}
    )
    
    return Reply(), 200

@v2acc.route("/password", methods=["POST"])
@Sessions.protect()
@Limiter.limit("3/hour")
def change_password():
    data = Require(request, password=str, newPassword=str).body()
    if not data.ok:
        return Reply(**data.content), 400
    
    user = Sessions.get_user(request.cookies.get("session"))
    if not HashStr(f"{user['_id']}${data.content['password']}") == user["password"]:
        return Reply(error="Current password is incorrect"), 400
    
    if len(data.content["newPassword"]) < 8:
        return Reply(error="Password too short"), 400
    
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {"$set": {"password": HashStr(f"{user['_id']}${data.content['newPassword']}")}}
    )
    
    return Reply(), 200