from events import ShellEventBus, EventBus
from ..helper import Helper

from core.logging import LoggingManager
from core.tools import ToDataUnit
from core.templates.UserTemplate import UserTemplate

import uuid
import os

logger = LoggingManager("Service.Shell")

@Helper.command("list", "List all users", "list")
@ShellEventBus.on("list")
def list_users(*args, **kwargs):
    from core import Database

    users = Database.get_database("xelapi").users.find()

    for user in users:
        updated = False
        for k, v in UserTemplate().items():
            if k not in user or (type(v) != type(user[k]) and v is not None):
                if type(v) is dict:
                    for kk, vv in v.items():
                        if kk not in user or (type(vv) != type(user[kk]) and vv is not None):
                            user[k][kk] = vv
                            updated = True
                
                user[k] = v
                updated = True    
        # this is a fucking abomination
            
        if updated:
            Database.get_database("xelapi").users.update_one({"_id": user["_id"]}, {"$set": {k: user[k]}})
            logger.warn(f"Updated user profile for {user['username']}")
                
        logger.info(f"{user['username']}{'*' if user['admin'] else ''} - {user['_id']} - {ToDataUnit(user['uploads']['storageUsed'])} (files: {len(user['uploads']['files'])}, max: {ToDataUnit(user['uploads'].get('storageMax', 0))})")
        
@Helper.command("term", "Terminate a user", "terminate <user_id>")
@ShellEventBus.on("term")
def terminate_user(*args, **kwargs):
    from core import Database, Config

    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    if not user:
        logger.warning(f"User not found")
        return
    
    for file in Database.get_database("xelapi").files.find({"author": args[0]}):
        os.remove(f"{Config.get('UPLOADS.PATH')}/{file['fullName']}")
        Database.get_database("xelapi").files.delete_one({"_id": file["_id"]})
        logger.success(f"File {file['fullName']} has been removed")

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
        
    
@Helper.command("rmfile", "Remove a file", "rmfile <file_id>")
@ShellEventBus.on("rmfile")
def remove_file(*args, **kwargs):
    from core import Database, Config

    file = Database.get_database("xelapi").files.find_one({"fullName": args[0]})
    if not file:
        file = Database.get_database("xelapi").files.find_one({"alias": args[0]})
        if not file:
            logger.warning(f"File not found")
            return

    os.remove(f"{Config.get('UPLOADS.PATH')}/{file['fullName']}")
    Database.get_database("xelapi").files.delete_one({"_id": file["_id"]})
    Database.get_database("xelapi").users.update_one(
        {"_id": file["author"]},
        {
            "$pull": {"uploads.files": file["fullName"]},
            "$inc": {"uploads.storageUsed": -file["size"]}
        }
    )
    logger.success(f"File {file['fullName']} has been removed")

@Helper.command("wipefiles", "Remove files from a user", "wipefiles <user_id>")
@ShellEventBus.on("wipefiles")
def wipe_files(*args, **kwargs):
    from core import Database, Config
    
    files = Database.get_database("xelapi").files.find({"author": args[0]})
    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    
    for file in files:
        os.remove(f"{Config.get('UPLOADS.PATH')}/{file['fullName']}")
        
        Database.get_database("xelapi").files.delete_one({"_id": file["_id"]})
        logger.success(f"File {file['fullName']} has been removed")
    
    if user:
        Database.get_database("xelapi").users.update_one({"_id": args[0]}, {"$set": {"uploads": {"files": [], "storageUsed": 0}}})
        logger.success(f"Files from {user['username']} have been removed")
        
@Helper.command("files", "List user's files", "files <user_id>")
@ShellEventBus.on("files")
def list_files(*args, **kwargs):
    from core import Database, Config

    files = Database.get_database("xelapi").files.find({"author": args[0]}).sort("size", -1)
    for file in files:
        logger.info(f"{file['fullName']} - {Config.get('SERVER.URL')}/upload/{file['alias']} - {ToDataUnit(file['size'])}")
        
@Helper.command("setmax", "Set user's max storage", "setmax <user_id> <size> <g|m|k|b>")
@ShellEventBus.on("setmax")
def set_max_storage(*args, **kwargs):
    from core import Database
    
    user = Database.get_database("xelapi").users.find_one({"_id": args[0]})
    if not user:
        logger.warning(f"User not found")
        return
    
    size = int(args[1])
    if args[2] == "g":
        size *= 1024 * 1024 * 1024
    elif args[2] == "m":
        size *= 1024 * 1024
    elif args[2] == "k":
        size *= 1024
    elif args[2] == "b":
        pass
    else:
        logger.warning(f"Invalid size unit")
        return
    
    Database.get_database("xelapi").users.update_one({"_id": args[0]}, {"$set": {"uploads.storageMax": size}})
    logger.success(f"Set max storage for {user['username']} to {ToDataUnit(size)}")