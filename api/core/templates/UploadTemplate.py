import json

def ShareXConfigTemplate(uploadKey):
    return json.dumps({
        "Name": "Xellu.tech",
        "DestinationType": "ImageUploader, FileUploader",
        
        "RequestType": "POST",
        "RequestURL": "https://xellu.tech/api/v2/files/upload",
        "FileFormName": "file",
        "Body": "MultipartFormData",
        "Headers": {
            "Authorization": uploadKey
        },
        "URL": "$json:url$",
        "DeletionURL": "$json:deleteUrl$",
        "ErrorMessage": "$json:error$"
    }, indent=4)
    
def FileTemplate():
    return {
        "alias": "example.png",
        "fullName": "7461595e95f347b6bccbb8e10b3760cf-example.png",
        "author": None,
        
        "size": 1024,
        "contentType": "image/png"
    }