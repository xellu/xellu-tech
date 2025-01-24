from events import ShellEventBus
from core.services.shell.helper import Helper

@ShellEventBus.on("diagnose")
@Helper.command(name="diagnose", description="Analyzes the whole system and returns a report, use --fix flag to attempt to fix issues", usage="diagnose [--fix]")
def diagnose(*args, **kwargs):
    from servers.http.router import Sessions
    from core.logging import LoggingManager
    
    logger = LoggingManager("Plugins.Diagnose")
    
    fix = kwargs.get("fix", False)
    
    if Sessions.sessions is None:
        logger.warn(f"Sessions are not initialized")
        if fix:
            from core import Database
            Sessions.sessions = Database.get_database("xelapi").sessions
            
    return "Diagnose complete"