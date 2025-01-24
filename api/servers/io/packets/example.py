from events import IOPacketBus
from core.logging import LoggingManager

import time

logger = LoggingManager("Server.Socket")

@IOPacketBus.on("heartbeat")
def heartbeat(client, data):
    client.last_heartbeat = time.time()

@IOPacketBus.on("hello")
def hello(client, data):
    logger.success(f"{client.ip}: Received hello packet")
    client.send(id="hello", data="world")