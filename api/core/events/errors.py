from events import EventBus
from core.logging import LoggingManager
from core.shared import CoreStats

import traceback

logger = LoggingManager("Core.Events")

fallback = {
    "source": "Nautica API",
    "message": "An error occurred in the Nautica API",
}

@EventBus.on("error")
def error_callback(error: Exception, source: str = fallback["source"], message: str = fallback["message"], fatal: bool = False):
    from core import Config
    from plugins.supervisor import SVClient

    logger.error(f"Error in {source}: {error}")

    trigger = None
    traces = []


    tracebacks = traceback.format_tb(tb=error.__traceback__)
    tbdata = traceback.extract_tb(error.__traceback__)
    
    if Config.get("DEVMODE"): logger.error("==========================================")

    for i, tb in enumerate(tracebacks):
        if Config.get("DEVMODE"): 
            logger.error(f"Traceback #{i+1}:")
            logger.error(tb)
            logger.error("==========================================")
        traces.append(tb)
    
    try:
        filename, linenum, funcname, linecontent = tbdata[-1]
        trigger = f"# File: {filename}\n# Line: {linenum}\n# Function: {funcname}\n\n{linecontent}"

        if Config.get("DEVMODE"): logger.error(f"Source: {filename} @ {linenum} in {funcname} -> {linecontent}")
    except:
        if Config.get("DEVMODE"): logger.error(f"Failed to parse traceback data")
    
    SVClient.send(
        id="error",
        error=f"{error}",
        traceback=traces if len(traces) > 0 else None,
        trigger=trigger
    )

    if fatal:
        EventBus.signal("shutdown.crash", f"Fatal error in {source}: {message}")