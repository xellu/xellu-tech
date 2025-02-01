import json
import time

def ShareXConfigTemplate(uploadKey):
    from core import Config
    
    return json.dumps({
        "Version": "17.0.0",
        "Name": "Xellu.tech",
        "DestinationType": "ImageUploader, FileUploader",
        
        "RequestType": "POST",
        "RequestURL": f"{Config.get('SERVER.URL')}/api/v2/files/upload",
        "FileFormName": "file",
        "Body": "MultipartFormData",
        "Headers": {
            "Authorization": uploadKey
        },
        "URL": "{json:url}",
        "DeletionURL": "{json:deleteUrl}",
        "ErrorMessage": "{json:error}"
    }, indent=4)
    
def FileTemplate():
    return {
        "alias": "example.png",
        "fullName": "7461595e95f347b6bccbb8e10b3760cf-example.png",
        "originalName": "example.png",
        "author": None,
        
        "size": 1024,
        "contentType": "image/png",
        
        "uploadedAt": time.time()
    }