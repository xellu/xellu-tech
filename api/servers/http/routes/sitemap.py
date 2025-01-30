from ..router import v2sitemap

from core import Config, Database

from flask import request, make_response
import time


@v2sitemap.route("/blog.xml", methods=["GET"])
def blog_sitemap():
    """
    Generates a sitemap for the blog
    """
    
    posts = list(Database.get_database("xelapi").blog.find().sort("createdAt", -1).limit(1024))

    #generate xml
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
    
    for post in posts:
        lastMod = post["createdAt"] if post["lastModified"] is None else post["lastModified"]
        
        xml += f"""<url>
    <loc>{Config.get("SERVER.URL")}/blog/{post["_id"]}</loc>
    <lastmod>{time.strftime('%Y-%m-%d', time.gmtime(lastMod))}</lastmod>
</url>
"""
    
    xml += "</urlset>"
    
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    
    return response