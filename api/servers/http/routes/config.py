from ..router import v2config, Sessions, Limiter
from ..services.adapter import Reply, Require

from core import Database, Config
from core.tools import RandomStr, HashStr
from core.templates.UploadTemplate import ShareXConfigTemplate

from flask import request, make_response

#downloads---
@v2config.route("/download/sharex", methods=["GET"]) #ShareX config
@Limiter.limit("5/minute")
@Sessions.protect()
def get_upload_config():
    user = Sessions.get_user(request.cookies.get("session"))
    
    #generate a session key (and also delete any old ones)
    key = f"{user['username']}.{RandomStr(4)}.{HashStr(RandomStr(16))}"
    
    Sessions.delete_all_matching_scope(user["_id"], "upload") 
    Sessions.create(user["_id"], scopes=["upload"], tokenOverride=key)
    
    data = ShareXConfigTemplate(key)
    
    r = make_response(data)
    r.headers["Content-Type"] = "application/octet-stream"
    r.headers["Content-Disposition"] = f"attachment; filename=xellutech-{user['username']}.sxcu"
    
    return r, 200

#settings------
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
        
        #embed text fields (string or None)
        elif key in ["embeds.title", "embeds.description", "embeds.siteName"]:
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
            
        else:
            return Reply(error=f"Unknown setting: {key}"), 400
        
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {
            "$set": {"settings": user["settings"]}
        }
    )
    
    return Reply(settings=user["settings"]), 200