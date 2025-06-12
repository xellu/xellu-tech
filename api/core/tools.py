import random
import string
import hashlib
import requests

from .config import ConfigManager

def RandomStr(length: int=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def HashStr(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

def LoadPlaceholders(text: str, config: ConfigManager):
    for key, value in config.data.items():
        text = text.replace(f"%{key}%", str(value))

    return text

def SanitizePath(path: str):
    return path.replace("..", "").replace("/", "").replace("\\", "")

def ToDataUnit(size: int):
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.1f}{unit}"
        size /= 1024

    return f"{size:.1f}PB"

def get_mc_uuid(username):
    """Get the UUID of a Minecraft account by username"""
    if not username:
        return None
    
    try:
        #DEPRECATED API
        # r = requests.get(f"https://mcprofile.io/api/v1/java/username/{username}")
        # r.raise_for_status()
        # data = r.json()
            
        # return data.get("uuid")

        r = requests.get(f"https://playerdb.co/api/player/minecraft/{username}")
        r.raise_for_status()
        data = r.json()
        
        return data.get("data", {}).get("id")
    except requests.RequestException as e:
        return None
    
def get_mc_username(uuid):
    """Get the username of a Minecraft account by UUID"""
    if not uuid:
        return None
    
    try:
        #DEPRECATED API
        # r = requests.get(f"https://mcprofile.io/api/v1/java/uuid/{uuid}")
        r = requests.get(f"https://playerdb.co/api/player/minecraft/{uuid}")
        r.raise_for_status()
        data = r.json()
        
        return data.get("data", {}).get("username") 
        # return data.get("username")
    except requests.RequestException as e:
        return None