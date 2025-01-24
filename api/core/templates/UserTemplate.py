import uuid
import time

def UserTemplate():
    return {
        "_id": str(uuid.uuid4()),
        
        "username": "",
        "password": "",
        
        "uploads": [],
        "admin": False,
        
        "created": time.time(),
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