import time
import uuid

def BlogPostTemplate():
    return {
        "_id": str(uuid.uuid4()),
        "createdAt": time.time(),
        "lastModified": None,
        
        "title": "",
        "brief": "",
        "content": "",
        
        "author": None, #user uuid
    }