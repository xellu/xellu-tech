from napi.http import HTTP, Require, Context, Reply, Error
from nautica import Config

from discord_webhook.async_webhook import AsyncDiscordWebhook
from discord_webhook import DiscordEmbed

@HTTP.POST()
@HTTP.Require(body = {
    "name": str,
    "email": Require.RegExMatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
    "service": Require.AnyOf("frontend", "backend", "fullstack", "ui", "other"),
    "budget": int,
    "content": str       
})
async def commissions(ctx: Context):
    customService = ctx.body.get("customService")
    if ctx.body["service"] == "other" and customService is None:
        raise Error(400, "No custom service provided")
    
    if len(ctx.body["name"]) > 64: raise Error(400)
    if len(ctx.body["email"]) > 128: raise Error(400)
    if customService and len(customService) > 128: raise Error(400)
    if len(ctx.body["content"]) > 1024: raise Error(400)
    if ctx.body["budget"] <= 0: raise Error(400)
    
    ctx.body['content'] = ctx.body['content'].replace("`", "\\`")
    
    if customService:
        customService = customService.replace("`", "\\`")
    
    hook = AsyncDiscordWebhook(url=Config("xyz")["contact.webhookUrl"])
    hook.add_embed(DiscordEmbed(
        title = "New Commission Inquiry",
        description = f"""
**Name:** {ctx.body['name']}
**Email:** {ctx.body['email']}
**Service:** {ctx.body['service']} {f'`{customService}`' if ctx.body['service'] == 'other' else ''}
**Budget:** {ctx.body['budget']}€
**Message:** ```
{ctx.body['content']}
```
        """
    ))
    await hook.execute()
    
@HTTP.POST()
@HTTP.Require(body = {
    "name": str,
    "email": Require.RegExMatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"),
    "content": str
})
async def contact(ctx: Context):
    if len(ctx.body["name"]) > 64: raise Error(400)
    if len(ctx.body["email"]) > 128: raise Error(400)
    if len(ctx.body["content"]) > 1024: raise Error(400)

    hook = AsyncDiscordWebhook(url=Config("xyz")["contact.webhookUrl"])
    hook.add_embed(DiscordEmbed(
        title = "New Message",
        description = f"""
**Name:** {ctx.body['name']}
**Email:** {ctx.body['email']}
**Message:** ```
{ctx.body['content'].replace("`", "\\`")}
```
        """
    ))
    await hook.execute()