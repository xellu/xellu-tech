from events import EventManager, EventBus

from core import Config
from core.logging import LoggingManager

import time
import json
import socket
import threading
import hashlib

logger = LoggingManager("Plugins.Supervisor")

def HashStr(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()

SPacketBus = EventManager(bounce=True)

class Client:
    def __init__(self, server_id: str = None):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_id = server_id

        self.connected = False
        self.authed = False
        self.last_heartbeat = 0

        self.retries = [5, 5, 5, 10, 20, 30, 60, 120]
        self.retry_index = 0

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((Config.get("SUPERVISOR")["HOST"], Config.get("SUPERVISOR")["SOCK.PORT"]))
            self.connected = True
            self.retry_index = 0

            logger.success("Connected to Supervisor")

            threading.Thread(target=self.event_loop).start()
            self.read_loop()
        except Exception as e:
            self.connected = False
            if self.retry_index < len(self.retries):
                self.retry_index += 1

                logger.warning(f"Failed to connect to Supervisor: {e}")
                logger.warning(f"Retrying supervisor connection in {self.retries[self.retry_index]} seconds.")
                EventBus.signal("error", e, "Plugins.Supervisor", "Unable to connect to Supervisor server", fatal=False)

                threading.Timer(self.retries[self.retry_index], self.connect).start()
            else:
                EventBus.signal("error", e, "Plugins.Supervisor", "Failed to connect to Supervisor after multiple retries", fatal=True)


    def read_loop(self):
        while True:
            if not self.connected:
                break

            try:
                data = self.sock.recv(65535)
                data = data.decode()
            except ConnectionResetError:
                self.drop("connection reset by peer")
                break
            except ConnectionAbortedError:
                self.drop("connection aborted")
                break
            except Exception as e:
                self.drop(f"read error ({e})")
                break

            if not data:
                self.drop("no data")
                break

            try:
                payload = json.loads(data)
            except Exception as e:
                self.drop(f"failed to parse ({e})")
                break
        
            if payload.get("id") is None:
                self.drop("bad packet")
                break

            try:
                logger.debug(f"IN ({(len(data)/1024):.2f}kb) <- {payload}")
                sent = SPacketBus.signal(payload["id"], self, payload)
                if not sent:
                    # self.send(id="error", error="Packet not processed")
                    break

            except Exception as e:
                # self.send(id="error", error=f"Failed to process packet: {e}")
                EventBus.emit("error", e, "Plugins.Supervisor", f"Failed to process packet: {e}")
                break

    def event_loop(self):
        while True:
            if not self.connected:
                break

            if self.last_heartbeat + 10 < time.time():
                self.send(id="heartbeat")
                self.last_heartbeat = time.time()
                
            time.sleep(1)

    def send(self, **kwargs):
        if not self.connected:
            return
        
        payload = json.dumps(kwargs)
        logger.debug(f"OUT ({(len(payload)/1024):.2f}kb) -> {kwargs}")

        try:
            self.sock.send(payload.encode())
        except Exception as e:
            self.drop(f"send error ({e})")

    def drop(self, reason: str):
        try:
            self.sock.close()
        except:
            pass

        self.connected = False
        self.authed = False
        logger.warning(f"Connection dropped: {reason}")
        logger.warning(f"Attempting to reconnect in 5 seconds.")
            
        threading.Timer(5, self.connect).start()

SVClient = Client("api")

# @EventBus.on("ready")
# def on_ready():
threading.Thread(target=SVClient.connect).start()

#packet handlers ------

@SPacketBus.on("error")
def packet_error(client, packet):
    logger.error(f"Supervisor error: {packet['content']}")

@SPacketBus.on("auth")
def packet_auth(client, packet):
    client.send(id="auth", server=client.server_id, key=HashStr(Config.get("SUPERVISOR")["ACCESS.KEY"]))

@SPacketBus.on("auth.ok")
def packet_auth_ok(client, packet):
    client.authed = True
    logger.success("Successfully authenticated with Supervisor")

@SPacketBus.on("shutdown")
def packet_shutdown(client, packet):
    EventBus.signal("shutdown", "Received shutdown command from Supervisor")