import uuid
import time

def UserTemplate():
    return {
        "_id": str(uuid.uuid4()),
        
        "username": "",
        "password": "",
        
        "admin": False,
        
        "uploads": {
            "files": [], #fileId[] - just a uuid
            "folders": [], #{name: "", files: fileId[]}
            "storageUsed": 0
        },
        "settings": {
            "embeds": {
                "enabled": True,
                "title": "Xellu.tech",
                "description": None,
                "siteName": None,
                "color": "#33A4F7",
            },
            "rawUrl": False
        },
        
        "createdAt": time.time(),
}    
    
def SanitizeUser(user: dict):
    """
    Removes all keys from a user object that are not in the UserTemplate and sensitive information
    """
    
    BLACKLIST = [
        "password"
    ]
    
    if not type(user) == dict:
        return None
    
    user = user.copy()
    
    for key in user.copy():
        if key not in UserTemplate():
            del user[key]
            
        if key in BLACKLIST:
            del user[key]
            
    return user