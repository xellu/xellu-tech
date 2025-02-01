from ..router import v2files, Sessions, Limiter
from ..services.adapter import Reply

from core import Config, Database
from core.tools import RandomStr, SanitizePath
from core.templates.UploadTemplate import FileTemplate
from core.templates.UserTemplate import UserTemplate

import os
import uuid
from flask import request, send_from_directory

#upload clients-----
@v2files.route("/upload", methods=["POST"]) #upload for ShareX/other clients
@Limiter.limit("30/minute")
def upload_file():
    session = request.headers.get("Authorization") if request.headers.get("Authorization") else request.cookies.get("session")
    user = Sessions.get_user(session, scopes=["upload"])
    if not user:
        return Reply(error="Authorization required"), 401
    
    file = request.files.get("file")
    if not file:
        return Reply(error="No file was provided") , 400

    alias = RandomStr(12)
    extension = SanitizePath(file.filename).split(".")[-1] if "." in file.filename else "bin"
    content = file.read()

    fd = FileTemplate()
    fd["alias"] = alias
    fd["fullName"] = f"{uuid.uuid4().hex}-{alias}.{extension}"
    fd["originalName"] = file.filename if file.filename else fd["fullName"]
    fd["author"] = user["_id"]
    
    fd["size"] = len(content)
    fd["contentType"] = file.content_type
    
    if user["uploads"]["storageUsed"] + fd["size"] > user["uploads"]["storageMax"]:
        return Reply(error="Storage limit reached"), 413
    
    with open(f"{Config.get('UPLOADS.PATH')}/{fd['fullName']}", "wb") as f:
        f.write(content)
        
    Database.get_database("xelapi").files.insert_one(fd)
    Database.get_database("xelapi").users.update_one(
        {"_id": user["_id"]},
        {
            "$push": {"uploads.files": fd["fullName"]},
            "$inc": {"uploads.storageUsed": fd["size"]}
        }
    )
        
    domainsAvailable = Config.get("UPLOADS.DOMAINS.AVAILABLE")
    domain = (f"{user['settings']['subDomain']}." if user['settings']['subDomain'] else "") + domainsAvailable[0] if user["settings"]["domain"] not in domainsAvailable else user["settings"]["domain"]
    baseUrl = f"{Config.get('UPLOADS.BASEURL').replace('%domain%', domain)}"
        
    return Reply(
        url = f"{baseUrl}/upload/{fd['alias']}" if not user['settings']['rawUrl'] else f"{baseUrl}/api/v2/files/{fd['fullName']}",
        deleteUrl = f"{Config.get('SERVER.URL')}/api/v2/files/delete/{fd['fullName']}",
    )    

@v2files.route("/delete/<file>", methods=["DELETE", "POST"]) #ShareX delete url
@Limiter.limit("30/minute")
def delete_file():
    session = request.headers.get("Authorization") if request.headers.get("Authorization") else request.cookies.get("session")
    user = Sessions.get_user(session, scopes=["upload"])
    if not user:
        return Reply(error="Authorization required"), 401
    
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

#file downloads-----
@v2files.route("/embed/<alias>", methods=["GET"]) #get file data using alias
@Limiter.limit("60/minute")
def get_file_using_alias(alias):
    file = Database.get_database("xelapi").files.find_one({"alias": alias})
    if not file:
        return Reply(error="File not found"), 404
    
    author = Database.get_database("xelapi").users.find_one({"_id": file["author"]})
    embedSettings = UserTemplate()["settings"]["embeds"] if not author else author["settings"]["embeds"]
    
    return Reply(
        fileUrl = f"{Config.get('SERVER.URL')}/api/v2/files/{file['fullName']}",
        fileName = file.get("originalName", file['fullName']),
        size = file["size"],
        uploadedAt = file.get("uploadedAt", 0),
        
        embed = embedSettings,
        author = {
            "_id": author["_id"],
            "username": author["username"]
        }
    )
    

@v2files.route("/<file>", methods=["GET"]) #file download
@Limiter.limit("60/minute")
def get_file(file):
    file = Database.get_database("xelapi").files.find_one({"fullName": file})
    if not file:
        return Reply(error="File not found"), 404
    
    return send_from_directory(Config.get("UPLOADS.PATH"), file["fullName"], as_attachment=True)