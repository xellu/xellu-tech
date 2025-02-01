from ..router import v2config, Sessions, Limiter
from ..services.adapter import Reply, Require

from core import Database, Config
from core.tools import RandomStr, HashStr
from core.templates.UploadTemplate import ShareXConfigTemplate

from flask import request, make_response
import re

def keyRegen(user):
    key = f"{user['username']}.{RandomStr(4)}.{HashStr(RandomStr(16))}"
    
    Sessions.delete_all_matching_scope(user["_id"], "upload") 
    Sessions.create(user["_id"], scopes=["upload"], tokenOverride=key)
    
    return key

#downloads---
@v2config.route("/download/sharex", methods=["GET"]) #ShareX config
@Limiter.limit("5/minute")
@Sessions.protect()
def get_upload_config():
    user = Sessions.get_user(request.cookies.get("session"))
    
    #get a key
    query = Sessions.sessions.find_one({"user_id": user["_id"], "scopes": "upload"})
    if not query:
        key = keyRegen(user)
    else:
        key = query["token"]
    
    data = ShareXConfigTemplate(key)
    
    r = make_response(data)
    r.headers["Content-Type"] = "application/octet-stream"
    r.headers["Content-Disposition"] = f"attachment; filename={user['username']}.xellu-tech.sxcu"
    
    return r, 200

#settings------
@v2config.route("/regenerate", methods=["POST"])
@Sessions.protect()
@Limiter.limit("5/minute")
def regenerate_upload_key():
    user = Sessions.get_user(request.cookies.get("session"))

    key = keyRegen(user)

    return Reply(key=key), 200

@v2config.route("/push", methods=["POST"])
@Sessions.protect()
def push_settings():
    user = Sessions.get_user(request.cookies.get("session"))
    
    data = Require(request, settings=dict).body()
    if not data.ok:
        return Reply(**data.content), 400
    
    for key, value in data.content["settings"].items():
        #embeds enabled (boolean)
        if key == "embeds.enabled":
            user["settings"]["embeds"]["enabled"] = bool(value)
        
        #embed title
        elif key == "embeds.title":
            if not value or type(value) != str:
                value = None
                user["settings"]["embeds"]["enabled"] = False
            
            user["settings"]["embeds"]["title"] = value
        
        #embed text fields (string or None)
        elif key in ["embeds.description", "embeds.siteName"]:
            if value is None or type(value) != str:
                value = None
                
            if len(str(value)) > 256:
                return Reply(error=f"{key} exceeds maximum allowed length"), 400
                
            user["settings"]["embeds"][key.split(".")[1]] = value
            
        #embed color (string - hex)
        elif key == "embeds.color":
            if not value:
                value = "#33A4F7" #default color
                
            if not value.startswith("#"):
                return Reply(error="Invalid color format"), 400
            
            if len(value) != 7:
                return Reply(error="Invalid color format"), 400
            
            user["settings"]["embeds"]["color"] = value
            
        #other booleans
        elif key in ["rawUrl"]:
            user["settings"][key] = bool(value)
            
        elif key == "domain":
            if not value:
                value = Config.get("UPLOADS.DOMAINS.AVAILABLE")[0]
                
            if value not in Config.get("UPLOADS.DOMAINS.AVAILABLE"):
                return Reply(error="Invalid domain"), 400
            
            user["settings"][key] = value
            
        elif key == "subDomain":
            if not value or type(value) != str:
                value = None
                
            if len(str(value)) > 64:
                return Reply(error="Subdomain exceeds maximum allowed length"), 400
                
            if not re.match(r"^[a-zA-Z0-9-]*$", str(value)):
                return Reply(error="Unicode not allowed"), 400
                
            user["settings"][key] = value
        else:
            return Reply(error=f"Unknown setting: {key}"), 400
        
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {
            "$set": {"settings": user["settings"]}
        }
    )
    
    return Reply(settings=user["settings"]), 200

@v2config.route("/available-domains", methods=["GET"])
def get_available_domains():
    r = Reply(domains=Config.get("UPLOADS.DOMAINS.AVAILABLE"))
    r.headers["Cache-Control"] = "max-age=86400"
    r.headers["Expires"] = "86400"
    
    return r, 200