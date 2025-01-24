import asyncio
import json
import threading
import time
import websockets
from core.logging import LoggingManager
from core import Config
from events import EventBus, WSPacketBus
from .packets import example

logger = LoggingManager("Server.WebSocket")
logger.info("Initializing WebSocket server")

class WebSocketClient:
    def __init__(self, websocket, path):
        self.client = websocket
        self.path = path

        self.ip = websocket.remote_address[0]
        self.port = websocket.remote_address[1]

        self.user = None

        self.running = False
        self.last_heartbeat = 0

        self.threads = []

    async def handle(self):
        self.running = True

        await self.read_loop()

    async def read_loop(self):
        while True:
            if not self.running:
                break

            try:
                data = await self.client.recv()
            except websockets.ConnectionClosed:
                await self.drop("connection closed")
                break
            except Exception as e:
                await self.drop(f"crashed ({e})")
                break

            if not data:
                await self.drop("no data received")
                break

            try:
                payload = json.loads(data)
                if not payload.get('id'):
                    await self.drop("no packet id")
                    break
            except:
                await self.drop("corrupted data")
                break

            try:
                processed = WSPacketBus.signal_async(payload.get('id'), self, payload)
            except Exception as e:
                await self.drop(f"handler crashed ({e})")
                break

            if not processed:
                await self.send(id="error", content="Packet not processed")
                
    async def send(self, **kwargs):
        if Config.get("DEVMODE"): logger.debug(f"{self.ip}: Sending -> {kwargs}")
        await self.client.send(json.dumps(kwargs))

    async def drop(self, reason: str = "dropped"):
        self.running = False
        logger.info(f"{self.ip}: Disconnected, {reason}")

        try:
            await self.client.close()
        except:
            pass

        threading.Thread(target=self.kill).start()

    def kill(self):
        self.running = False

class WebSocketServer:
    def __init__(self):
        self.running = False

    async def start(self):
        self.running = True

        async with websockets.serve(self.handler, Config.get("HTTP.HOST"), Config.get("WS.PORT")):
            await asyncio.Future()  # Run forever

    async def handler(self, websocket, path):
        client = WebSocketClient(websocket, path)
        await client.handle()

    @EventBus.on("shutdown")
    def on_shutdown(reason: str | None = None):
        logger.ok("Offline")
        Server.running = False

Server = WebSocketServer()

@WSPacketBus.listen_all
async def packet_debugger(event, client, data):
    if Config.get("DEVMODE"): logger.debug(f"{client.ip}: {event} -> {data}")