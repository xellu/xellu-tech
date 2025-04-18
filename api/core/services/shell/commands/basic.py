from events import ShellEventBus, EventBus
from ..helper import Helper

from core.logging import LoggingManager, path as logpath
from importlib import reload

import os

logger = LoggingManager("Service.Shell")

#help command
@Helper.command("help", "List all available commands & their usage", "help [command]")
@ShellEventBus.on("help")
def help_command(*args, **kwargs):
    if len(args) > 0:
        command = args[0]
        if command not in Helper.commands:
            logger.warning(f"Command '{command}' not found")
            return

        logger.info("<> - Required, [] - Optional")
        logger.info(f"{command} - {Helper.commands[command]['description']}")
        logger.info(f"Usage: {Helper.commands[command]['usage']}")
        return


    logger.info("<> - Required, [] - Optional")
    logger.info("Showing available commands:")
    for key, value in Helper.commands.items():
        logger.info(f"  {value['usage']} - {value['description']}")

#stop command
@Helper.command("stop", "Stops the server", "stop [--force]")
@ShellEventBus.on("stop")
def stop_command(*args, **kwargs):
    if kwargs.get("force", False):
        EventBus.signal("shutdown.force", "Requested by admin")
        return
    
    EventBus.signal("shutdown", "Requested by admin")

#clear logs
@Helper.command("clearlogs", "Delete previous logs", "clearlogs")
@ShellEventBus.on("clearlogs")
def clear_logs(*args, **kwargs):
    amount = 0
    for file in os.listdir(".logs"):
        if file == logpath:
            continue

        os.remove(f".logs/{file}")
        amount += 1
    
    logger.success(f"Deleted {amount} logs")

#clear console
@Helper.command("clear", "Clear the console", "clear")
@ShellEventBus.on("clear")
def clear_console(*args, **kwargs):
    os.system("cls" if os.name == "nt" else "clear")
    
#revoke all sessions
@Helper.command("resetsessions", "Revokes all sessions", "resetsessions")
@ShellEventBus.on("resetsessions")
def clear_all_sessions(*args, **kwargs):
    from core import Database
    
    
    if Database.get_database("sessions") is None:
        logger.warning("Database not loaded")
    
    Database.get_database("xelapi").sessions.delete_many({})
    logger.success("done")
    
#rekove all rate limits
@Helper.command("resetratelimits", "Revokes all rate limits", "resetratelimits")
@ShellEventBus.on("resetratelimits")
def clear_all_ratelimits(*args, **kwargs):
    from core import Database
    
    if Database.get_database("limits") is None:
        logger.warning("Database not loaded")
    
    Database.get_database("limits").counters.delete_many({})
    Database.get_database("limits").windows.delete_many({})
    logger.success("done")