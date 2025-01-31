from ..router import v2files, Sessions, Limiter
from ..services.adapter import Reply, Require

from core import Config, Database
from core.tools import RandomStr, HashStr, SanitizePath
from core.templates.UploadTemplate import ShareXConfigTemplate, FileTemplate

import os
import uuid
from flask import request, make_response, send_from_directory

#upload clients-----
@v2files.route("/upload", methods=["POST"]) #upload for ShareX/other clients
@Limiter.limit("30/minute")
def upload_file():
    session = request.headers.get("Authorization") if request.headers.get("Authorization") else request.cookies.get("session")
    user = Sessions.get_user(session, scopes=["upload"])
    
    file = request.files.get("file")
    if not file:
        return Reply(error="No file was provided")

    alias = RandomStr(12)
    extension = SanitizePath(file.filename).split(".")[-1] if "." in file.filename else "bin"

    fd = FileTemplate()
    fd["alias"] = alias
    fd["fullName"] = f"{uuid.uuid4().hex}-{alias}.{extension}"
    fd["author"] = user["_id"]
    
    fd["size"] = file.content_length
    fd["contentType"] = file.content_type
    
    file.save(f"{Config.get('UPLOADS.PATH')}/{fd['fullName']}")
    Database.get_database("xelapi").files.insert_one(fd)
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {
            "$push": {"uploads.files": fd["fullName"]},
            "$inc": {"uploads.storageUsed": fd["size"]}
        }
    )
        
    return Reply(
        url = f"{Config.get('SERVER.URL')}/upload/{fd['alias']}" if not user['settings']['rawUrl'] else f"{Config.get('SERVER.URL')}/api/v2/files/{fd['fullName']}",
        deleteUrl = f"{Config.get('SERVER.URL')}/api/v2/files/delete/{fd['fullName']}",
    )    

@v2files.route("/delete/<file>", methods=["DELETE", "POST"]) #ShareX delete url
@Limiter.limit("30/minute")
def delete_file():
    session = request.headers.get("Authorization") if request.headers.get("Authorization") else request.cookies.get("session")
    user = Sessions.get_user(session, scopes=["upload"])
    
    file = Database.get_database("xelapi").files.find_one({"fullName": file})
    if not file:
        return Reply(error="File not found"), 404
    
    if file["author"] != user["_id"]:
        return Reply(error="Insufficient permissions"), 403
    
    Database.get_database("xelapi").files.delete_one({"fullName": file})
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {
            "$pull": {"uploads.files": file["fullName"]},
            "$inc": {"uploads.storageUsed": -file["size"]}
        }
    )
    
    os.remove(f"{Config.get('UPLOADS.PATH')}/{file['fullName']}")
    return Reply(), 200
    
  
#config downloads-----
@v2files.route("/config/sharex", methods=["GET"]) #ShareX config
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

#file downloads-----
@v2files.route("/")

@v2files.route("/alias/<alias>", methods=["GET"]) #file download
@Limiter.limit("60/minute")
def get_file_using_alias(alias):
    file = Database.get_database("xelapi").files.find_one({"alias": alias})
    if not file:
        return Reply(error="File not found"), 404
    
    return send_from_directory(Config.get("UPLOADS.PATH"), file["fullName"], as_attachment=True)

@v2files.route("/<file>", methods=["GET"]) #file download
@Limiter.limit("60/minute")
def get_file(file):
    file = Database.get_database("xelapi").files.find_one({"fullName": file})
    if not file:
        return Reply(error="File not found"), 404
    
    return send_from_directory(Config.get("UPLOADS.PATH"), file["fullName"], as_attachment=True)