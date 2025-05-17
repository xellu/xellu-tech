from ..router import v2clockbot, Limiter
from ..services.adapter import Reply, Require

from core import Database, Config
from core.tools import get_mc_uuid
from core.templates.Clockwork import WhitelistApplicationTemplate, ALLOWED_AGE_ANSWERS, ALLOWED_REGION_ANSWERS

from flask import request
import requests

@v2clockbot.route("/mc-profile/<username>", methods=["GET"])
def get_mc_profile(username):    
    uuid = get_mc_uuid(username)
    if not uuid:
        return Reply(error="Invalid username"), 400
    
    return Reply(uuid=uuid), 200

@v2clockbot.route("/discord/<exchange_code>", methods=["POST"])
def fetch_discord_user(exchange_code):
    r = requests.post(f"https://discord.com/api/oauth2/token", data={
        "client_id": Config.get("CW.DISCORD.APP.ID"),
        "client_secret": Config.get("CW.DISCORD.APP.SECRET"),
        "grant_type": "authorization_code",
        "code": exchange_code,
        "redirect_uri": f"{Config.get('SERVER.URL')}/clockwork",
    })
    
    if r.status_code != 200:
        return Reply(error=r.json().get("error_description", 'Failed to authorize')), 400
    
    data = r.json()
    if "access_token" not in data:
        return Reply(error="Unknown exchange format"), 400
    
    access_token = data["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    r = requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    if r.status_code != 200:
        return Reply(error=r.json().get("error_description", "Failed to get account data")), 400
    
    data = r.json()
    if "id" not in data:
        return Reply(error="No data found"), 400
    
    return Reply(
        id=data["id"],
        username=data["username"],
        avatar=data["avatar"]
    )

@v2clockbot.route("/apply", methods=["POST"])
# @Limiter.limit("2/minute")
def apply_for_whitelist():
    data = Require(request=request, 
        discord = str,
        minecraft = str,
        answers = dict
    ).body()
    
    if not data.ok:
        return Reply(**data.content), 400
    
    apply = WhitelistApplicationTemplate()
    apply["discord"] = int(data.content["discord"])
    apply["minecraft"] = data.content["minecraft"]
    
    for key in apply["answers"].keys():
        if key not in data.content["answers"].keys():
            return Reply(error=f"Missing answer for {key}"), 400
        
        
        if key == "age":
            if data.content["answers"][key] not in ALLOWED_AGE_ANSWERS:
                return Reply(error=f"Invalid answer for {key}"), 400
        
        if key == "region":            
            if data.content["answers"][key] not in ALLOWED_REGION_ANSWERS:
                return Reply(error=f"Invalid answer for {key}"), 400
        
        if key in ["howFound", "goodAt", "friendsPlaying"]:
            if len(str(data.content["answers"][key])) > 256:
                return Reply(error=f"Answer for {key} is too long"), 400
            
        if key in ["playedSMPs", "playedCreate"]:
            if not isinstance(data.content["answers"][key], bool) and data.content["answers"][key] is not None:
                return Reply(error=f"Answer for {key} must be a boolean"), 400
            
        if len(str(data.content["answers"][key])) > 512:
            return Reply(error=f"Answer for {key} is too long"), 400

    apply["answers"] = data.content["answers"]
    Database.get_database("clockbot").whitelist.insert_one(apply)

    return Reply(), 200
        
    
    