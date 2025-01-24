from .supervisor import SVClient, SPacketBus
from events import EventBus, EventManager
from core.logging import LoggingManager

import threading
import time
import uuid
import json
import asyncio

logger = LoggingManager("Plugins.Intercom")

class IntercomClient:
    def __init__(self):
        self.queue = []
        
        self.callbacks = {
            #ref_id: callback
        }
        
        self.handlers = {
            #id: handler
        }
        
    def send(self, destination, data, callback=None):
        """
        Send a message through the intercom system
        
        # Arguments
        destination (str): Server ID of the target server
        data (dict): The data to send (must be serializable)
        callback (function): A function to call when a reply is received
        """
        
        ref = f"{SVClient.server_id.upper()}.{uuid.uuid4()}"        
        self.callbacks[ref] = callback

        if not SVClient.authed:
            self.queue.append({"id": "intercom.send", "server_id": destination, "ref": ref, "data": data})
            logger.debug(f"Queued an outgoing intercom msg to {destination}")
            return
        
        SVClient.send(id="intercom.send", server_id=destination, ref=ref, data=data)
        
    async def send_and_wait_async(self, destination, data):
        """
        Send a message through the intercom system and wait for a reply
        
        # Arguments
        destination (str): Server ID of the target server
        data (dict): The data to send (must be serializable)
        """
        
        response = None
        def callback(data):
            nonlocal response
            response = data
            
        self.send(destination, data, callback)
        
        while True:
            if response is not None:
                break
            await asyncio.sleep(1)
        
        return response
    
    def send_and_wait(self, destination, data):
        """
        Send a message through the intercom system and wait for a reply
        
        # Arguments
        destination (str): Server ID of the target server
        data (dict): The data to send (must be serializable)
        """
        
        response = None
        timeout = time.time() + 15
        def callback(data):
            nonlocal response
            response = data
            
        self.send(destination, data, callback)
        
        while True:
            if response is not None:
                break
            if time.time() > timeout:
                break
            time.sleep(0.1)
        
        return response
        
    def reply(self, ref, data):
        """
        Reply to an intercom message using a reference ID
        
        # Arguments
        ref (str): Reference ID of the message
        data (dict): The data to send (must be serializable)
        """
        
        if not SVClient.authed:
            self.queue.append({"id": "intercom.reply", "ref": ref, "data": data})
            logger.debug(f"Queued an outgoing intercom reply to {ref}")
            return
        
        SVClient.send(id="intercom.reply", ref=ref, data=data)
        
    def on(self, id):
        """
        Decorator to register a handler for a specific intercom message ID
        
        # Arguments
        id (str): The ID of the message to handle
        """
        
        def wrapper(func):
            self.handlers[id] = func
            return func
        
        return wrapper
        
    def packet(self, **kwargs):
        """
        Returns a dictionary with the packet structure for an intercom message
        """
        
        return kwargs
        
    def event_loop(self):
        while True:
            
            #process queued messages
            if SVClient.authed and len(self.queue) > 0:
                logger.debug(f"Processing {len(self.queue)} queued intercom messages")
                
                for packet in self.queue:
                    SVClient.send(**packet)
                    self.queue.remove(packet)
                    
            time.sleep(1)
    
Intercom = IntercomClient()

@EventBus.on("ready")
def on_ready():
    threading.Thread(target=Intercom.event_loop).start()
    
#packet handler -------
@SPacketBus.on("intercom.send")
def on_request(client, packet):
    try:
        data = packet["data"]
        response = Intercom.handlers.get(data["id"])(client, packet)
        if type(response) is dict:
            Intercom.reply(packet["ref"], response)
            
    except Exception as e:
        EventBus.emit("error", e, "Plugins.Intercom", f"Failed to process intercom request: {e}")
        
        Intercom.reply(packet["ref"], {"id": "error", "error": "internal error"})
        
@SPacketBus.on("intercom.reply")
def on_reply(client, packet):
    if packet["data"].get("_type") is None:
        packet["data"]["_type"] = "reply"
    
    callback = Intercom.callbacks.get(packet["ref"])
    if callback is not None:
        callback(packet["data"])
        Intercom.callbacks.pop(packet["ref"])
     
@SPacketBus.on("intercom.error")
def on_error(client, packet):
    if not packet.get("data"): #create a data field if it doesn't exist
        packet["data"] = { "error": packet.get("error") or packet.get("content") or "unknown error" }
        
    packet["data"]["_type"] = "error"
    
    callback = Intercom.callbacks.get(packet["ref"])
    if callback is not None:
        callback(packet["data"])
        Intercom.callbacks.pop(packet["ref"])