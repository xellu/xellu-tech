from ..router import v2example, Sessions
from ..services.adapter import Reply, Require

from core import Database

from flask import request

@v2example.route("/login")
def session_login():
    #this route is used to create a session for the user
    #this route will return a session token that can be used to access protected routes

    data = Require(request, user_id=str).query()
    if not data.ok:
        return Reply(error="No user ID provided")

    if Database.get_database("users").users.find_one({"_id": data.content["user_id"]}) is None:
        user = {
            "_id": data.content["user_id"],
            "name": "User"
        }

        Database.get_database("users").users.insert_one(user)

    token = Sessions.create(data.content["user_id"])
    r = Reply(ok=True, token=token)
    r.set_cookie("session", token)

    return r

@v2example.route("/protected")
@Sessions.protect()
def session_protected():
    #this route is protected by the session service
    #if the session is invalid, the route will return a 401

    return Reply(message="You are authenticated!")

@v2example.route("/unprotected")
# @Sessions.with_user()
def session_unprotected():
    #this route is NOT protected by the session service
    #anyone can access this route

    user = Sessions.get_user(request.cookies.get("session"))

    if user:
        return Reply(message="You ARE authenticated")

    return Reply(message="You are NOT authenticated")