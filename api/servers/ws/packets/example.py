from events import WSPacketBus, EventBus

@WSPacketBus.on("hello")
async def hello(client, data):
    await client.send(
        id = "hello",
        content = "world"
    )    