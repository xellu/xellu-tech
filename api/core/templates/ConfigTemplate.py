ConfigTemplate = {
    "SERVER.NAME": "XelAPI",
    "DEVMODE": True,
    "SERVER.URL": "http://localhost",
    "UPLOADS.PATH": ".uploads/",
    
    "HTTP.HOST": "0.0.0.0",
    "HTTP.PORT": 3000,
    "SOCK.PORT": 3100,
    "WS.PORT": 3200,
    "HTTP.REAL.IP": "X-Real-IP",

    "DATABASE.URI": "mongodb+srv://%DATABASE.USER%:%DATABASE.USER%@cluster0.tayqoig.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    "DATABASE.USER": "",
    "DATABASE.PASS": "",
    
    "AUTH.EXPIRE": 7 * 24 * 60 * 60, #7 days
}