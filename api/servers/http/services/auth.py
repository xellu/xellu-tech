from core import Database, DatabaseService
from core.tools import HashStr, RandomStr
from events import EventBus

from.adapter import Reply

import time
from flask import request

class SessionService:
    def __init__(self):
        self.sessions = None

    #decorator to require a session authentication for a route
    def protect(self, look_for: str="session", method: str="cookie", scopes: list[str]=[]):
        """
        Protects a route with session authentication.
        Use as a decorator.
        
        Args:
            look_for (str): The name of the session token to look for.
            method (str): The method to look for the session token. Can be "cookie" or "header".
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                token = None

                if method == "cookie":
                    token = request.cookies.get(look_for)
                elif method == "header":
                    token = request.headers.get(look_for)

                if not token:
                    return Reply(error="Session not provided"), 401

                user_id = self.get(token, scopes=scopes)
                if not user_id:
                    return Reply(error="Session expired, or is invalid"), 401

                return func(*args, **kwargs)
            wrapper.__name__ = func.__name__
            return wrapper
        return decorator
    
    def create(self, user_id: str, expire: int | None = None, scopes: list[str] = []) -> str:
        """
        Creates a new session for the user.

        Args:
            user_id (str): The user ID to create the session for.
            expire (int | None): The expiration time for the session. Won't expire if set to None.

        Returns:
            str: The session token.
        """

        token = HashStr(RandomStr(32))
        self.sessions.insert_one({
            "user_id": user_id,
            "token": token,
            "expire": expire,
            "scopes": scopes,
        })

        return token

    def get(self, token: str, scopes: list[str] = []) -> str:
        """
        Gets the user ID from the session token.

        Args:
            token (str): The session token to get the user ID from.

        Returns:
            str: The user ID.
        """

        query = self.sessions.find_one({"token": token})
        if not query:
            return None
        
        if query["expire"] and query["expire"] < time.time():
            self.delete(token)
            return None
        
        if scopes and "*" not in query["scopes"]:
            for scope in scopes:
                if scope not in query["scopes"]:
                    return None

        return query["user_id"]
    
    def get_user(self, token: str, scopes: list[str] = []) -> dict:
        """
        Gets the user object from the session token.

        Args:
            token (str): The session token to get the user object from.

        Returns:
            dict: The user object.
        """

        user_id = self.get(token, scopes=scopes)
        if not user_id:
            return None
        
        user = Database.get_database("xelapi").users.find_one({"_id": user_id})

        return user
    
    def delete(self, token: str) -> None:
        """
        Deletes a session.

        Args:
            token (str): The session token to delete.
        """

        self.sessions.delete_one({"token": token})

    def delete_all(self, user_id: str) -> None:
        """
        Deletes all sessions for a user.

        Args:
            user_id (str): The user ID to delete all sessions for.
        """

        self.sessions.delete_many({"user_id": user_id})

    def delete_all_except(self, user_id: str, except_token: str) -> None:
        """
        Deletes all sessions for a user except for one.

        Args:
            user_id (str): The user ID to delete all sessions for.
            except_token (str): The session token to exclude from deletion.
        """

        self.sessions.delete_many({"user_id": user_id, "token": {"$ne": except_token}})
