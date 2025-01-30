from events import ShellEventBus, EventBus
from ..helper import Helper

from core.logging import LoggingManager

import uuid

logger = LoggingManager("Service.Shell")

@Helper.command("list", "List all users", "list")
@ShellEventBus.on("list")
def list_users(*args, **kwargs):
    from core import Database

    users = Database.get_database("xelapi").users.find()

    for user in users:
        logger.info(f"{user['username']} - {user['_id']} - {'Admin' if user['admin'] else 'User'}")
        
@Helper.command("term", "Terminate a user", "terminate <user_id>")
@ShellEventBus.on("term")
def terminate_user(*args, **kwargs):
    from core import Database

    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    if not user:
        logger.warning(f"User not found")
        return

    Database.get_database("xelapi").users.delete_one({"_id": args[0]})
    logger.success(f"User {user['username']} has been terminated")
    
@Helper.command("mkadmin", "Set a user as admin", "mkadmin <user_id>")
@ShellEventBus.on("mkadmin")
def make_admin(*args, **kwargs):
    from core import Database

    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    if not user:
        logger.warning(f"User not found")
        return

    Database.get_database("xelapi").users.update_one({"_id": args[0]}, {"$set": {"admin": True}})
    logger.success(f"Made {user['username']} an admin")
    
@Helper.command("rmadmin", "Remove a user as admin", "rmadmin <user_id>")
@ShellEventBus.on("rmadmin")
def remove_admin(*args, **kwargs):
    from core import Database

    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    if not user:
        logger.warning(f"User not found")
        return

    Database.get_database("xelapi").users.update_one({"_id": args[0]}, {"$set": {"admin": False}})
    logger.success(f"Removed admin from {user['username']}")
    
@Helper.command("mkinv", "Generate an invite code", "mkinv [count=1]")
@ShellEventBus.on("mkinv")
def make_invite(*args, **kwargs):
    from core import Database, Config
    import random

    count = 1
    if len(args) > 0:
        count = int(args[0])

    for i in range(count):
        code = str(uuid.uuid4())
        
        Database.get_database("xelapi").invites.insert_one({"code": code})
        logger.info(f"Invite code: {code} ({Config.get('SERVER.URL')}/invite/{code})")

@Helper.command("rminv", "Remove an invite code", "rminv <code|*>")
@ShellEventBus.on("rminv")
def remove_invite(*args, **kwargs):
    from core import Database
    
    if len(args) == 0:
        logger.warning("No invite code provided")
        return

    if args[0] == "*":
        Database.get_database("xelapi").invites.delete_many({})
        logger.success("All invites have been removed")
        return

    invite = Database.get_database("xelapi").invites.find_one({"code": args[0]})
    if not invite:
        logger.warning("Invite not found")
        return

    Database.get_database("xelapi").invites.delete_one({"code": args[0]})
    logger.success(f"Invite {args[0]} has been removed")
    
@Helper.command("lsinv", "List all invite codes", "lsinv")
@ShellEventBus.on("lsinv")
def list_invites(*args, **kwargs):
    from core import Database

    invites = Database.get_database("xelapi").invites.find()

    for invite in invites:
        logger.info(f"{invite['code']}")