import uuid
import time
from events import WSPacketBus, ShellEventBus
from core.services.shell.helper import Helper
from core.logging import LoggingManager

logger = LoggingManager("WS.AirLyft")

def AircraftTemplate(_id):
    return {
        "id": _id,
        "pos": {
            "x": 0,
            "y": 0,
            "z": 0
        },
        "goto": {
            "x": 0,
            "y": 0,
            "z": 0,
            "dist": 0
        },
        "fuel": 15,
        "status": "idle",
        "statusExpire": None,
        #idle        - on ground, empty
        #enroutePsg  - flying to passenger
        #waitPsg     - arrived, waiting for passenger to board
        #enrouteDst  - flying to destination
        #waitDst     - arrived at destination, waiting for passenger to exit
        "session": None,
        "lastPing": time.time()
    }

Aircrafts = []
Locations = [
    {"name": "Spawn", "x": -32, "y": 0, "z": 64},
    {"name": "The Hive, East Side", "x": -1500, "y": 0, "z": 2000},
]

# session_id -> { id, aircraft, status, created }
# session status: pending | boarding | active | completed | expired
FlightSessions = {}


def _new_session(aircraft_id):
    sid = uuid.uuid4().hex[:8]
    FlightSessions[sid] = {
        "id": sid,
        "aircraft": aircraft_id,
        "status": "pending",
        "created": time.time(),
    }
    return FlightSessions[sid]


def _clear_session(session_id, mark_status="completed"):
    sess = FlightSessions.get(session_id)
    if not sess:
        return
    sess["status"] = mark_status
    ac = next((a for a in Aircrafts if a["id"] == sess["aircraft"]), None)
    if ac:
        ac["session"] = None
    FlightSessions.pop(session_id, None)


def getAC(_id):
    now = time.time()
    # Collect stale entries first to avoid mutating list mid-iteration
    stale = [a for a in Aircrafts if a["lastPing"] < now - 10]
    for a in stale:
        if a["session"]:
            _clear_session(a["session"], mark_status="expired")
        Aircrafts.remove(a)
    return next((a for a in Aircrafts if a["id"] == _id), None)


@WSPacketBus.on("air.ping")
async def on_ping(client, data):
    ac = getAC(data["_id"])
    if not ac:
        ac = AircraftTemplate(data["_id"])
        ac["goto"] = { "x": data["x"], "y": data["y"], "z": data["z"], "dist": 0 }
        Aircrafts.append(ac)

    ac["pos"] = { "x": data["x"], "y": data["y"], "z": data["z"] }
    ac["lastPing"] = time.time()

    if ac["statusExpire"] and ac["statusExpire"] < time.time():
        prev = ac["status"]
        ac["status"] = "idle"
        ac["statusExpire"] = None
        if ac["session"]:
            # waitDst expiry means the ride finished and passenger has exited
            mark = "completed" if prev == "waitDst" else "expired"
            _clear_session(ac["session"], mark_status=mark)
        logger.info(f"Aircraft '{ac['id']}' status expired (was {prev})")

    if data.get("dist"):
        ac["goto"]["dist"] = data["dist"]

    await client.send(id="air.goto", x=ac["goto"]["x"], y=ac["goto"]["y"], z=ac["goto"]["z"])


@WSPacketBus.on("air.ride.request")
async def on_ride_request(client, data):
    px, py, pz = float(data["x"]), float(data["y"]), float(data["z"])

    def dist(ac):
        dx = ac["pos"]["x"] - px
        dz = ac["pos"]["z"] - pz
        return (dx**2 + dz**2) ** 0.5

    idle = [a for a in Aircrafts if a["status"] == "idle"]
    if not idle:
        await client.send(id="air.ride.request", error="No aircraft available")
        return

    ac = min(idle, key=dist)
    
    

    sess = _new_session(ac["id"])
    ac["session"] = sess["id"]
    
    if dist(ac) > 200:
        ac["status"] = "enroutePsg"
        ac["goto"] = { "x": px, "y": py, "z": pz, "dist": dist(ac) }
    else:
        ac["status"] = "waitPsg"
        sess["status"] = "boarding"

    await client.send(id="air.ride.request", aircraft=ac["id"], session=sess["id"])

@WSPacketBus.on("air.ride.start")
async def on_ride_start(client, data):
    session_id = data.get("session")
    if not session_id:
        await client.send(id="air.ride.start", error="No session ID provided")
        return

    sess = FlightSessions.get(session_id)
    if not sess:
        await client.send(id="air.ride.start", error="Invalid or expired session")
        return

    if sess["status"] != "boarding":
        status = sess["status"]
        if status == "pending":
            await client.send(id="air.ride.start", error="Aircraft has not arrived yet")
        elif status == "active":
            await client.send(id="air.ride.start", error="Ride already in progress")
        else:
            await client.send(id="air.ride.start", error=f"Session not ready ({status})")
        return

    ac = next((a for a in Aircrafts if a["id"] == sess["aircraft"]), None)
    if not ac:
        _clear_session(session_id, mark_status="expired")
        await client.send(id="air.ride.start", error="Aircraft no longer available")
        return

    if ac["status"] != "waitPsg":
        await client.send(id="air.ride.start", error="Aircraft is not waiting for a passenger")
        return

    dx = float(data["x"]) - ac["pos"]["x"]
    dy = float(data["y"]) - ac["pos"]["y"]
    dz = float(data["z"]) - ac["pos"]["z"]
    d = (dx**2 + dy**2 + dz**2) ** 0.5

    ac["status"] = "enrouteDst"
    ac["statusExpire"] = None
    ac["goto"] = { "x": float(data["x"]), "y": float(data["y"]), "z": float(data["z"]), "dist": d }

    sess["status"] = "active"

    await client.send(id="air.ride.start", aircraft=ac["id"], session=session_id)

@WSPacketBus.on("air.ride.cancel")
async def on_ride_cancel(client, data):
    session_id = data.get("session")
    if not session_id:
        await client.send(id="air.ride.cancel", error="No session ID provided")
        return

    sess = FlightSessions.get(session_id)
    if not sess:
        await client.send(id="air.ride.cancel", ok=True)  # already gone, that's fine
        return

    ac = next((a for a in Aircrafts if a["id"] == sess["aircraft"]), None)
    if ac:
        ac["status"] = "idle"
        ac["statusExpire"] = None
        ac["goto"] = { "x": ac["pos"]["x"], "y": ac["pos"]["y"], "z": ac["pos"]["z"], "dist": 0 }

    _clear_session(session_id, mark_status="cancelled")
    logger.info(f"Session '{session_id}' cancelled by passenger")
    await client.send(id="air.ride.cancel", ok=True)

@WSPacketBus.on("air.ride.status")
async def on_ride_status(client, data):
    session_id = data.get("session")
    if not session_id:
        await client.send(id="air.ride.status", error="No session ID provided")
        return

    sess = FlightSessions.get(session_id)
    if not sess:
        await client.send(id="air.ride.status", error="Session not found")
        return

    ac = next((a for a in Aircrafts if a["id"] == sess["aircraft"]), None)

    payload = {
        "id": "air.ride.status",
        "session": session_id,
        "status": sess["status"],
        "aircraft": sess["aircraft"],
    }
    if ac:
        payload["dist"] = ac["goto"]["dist"]
        payload["acStatus"] = ac["status"]

    await client.send(**payload)

@WSPacketBus.on("air.locations")
async def on_locations(client, _):
    await client.send(id="air.locations", locations=Locations)

@WSPacketBus.on("air.onLand")
async def on_land(client, data):
    ac = getAC(data["_id"])
    if not ac:
        return

    if ac["status"] == "enroutePsg":
        ac["status"] = "waitPsg"
        ac["statusExpire"] = time.time() + 120  # 2 min for passenger to board
        if ac["session"]:
            sess = FlightSessions.get(ac["session"])
            if sess:
                sess["status"] = "boarding"
    elif ac["status"] == "enrouteDst":
        ac["status"] = "waitDst"
        ac["statusExpire"] = time.time() + 60  # session stays "completed" until this expires
        if ac["session"]:
            sess = FlightSessions.get(ac["session"])
            if sess:
                sess["status"] = "completed"
    else:
        ac["status"] = "idle"
        ac["statusExpire"] = None
        if ac["session"]:
            _clear_session(ac["session"], mark_status="completed")

    logger.info(f"Aircraft '{ac['id']}' status -> {ac['status']}")


@ShellEventBus.on("ac.send")
@Helper.command("ac.send", "request an aircraft to position", "ac.send <id> <x> <z>")
def request_aircraft(*args, **kwargs):
    _id, x, z = args[0], args[1], args[2]

    ac = getAC(_id)
    if ac["status"] != "idle" and not kwargs.get("force"):
        logger.error("Aircraft is already enroute, use --force flag to ignore")

    ac["status"] = "enrouteDst"
    ac["goto"]["x"] = x
    ac["goto"]["y"] = 0
    ac["goto"]["z"] = z
    logger.ok("Aircraft requested")

@ShellEventBus.on("ac.land")
@Helper.command("ac.land", "land an aircraft at its current position", "ac.land <id>")
def land_ac(*args, **kwargs):
    _id = args[0]

    ac = getAC(_id)
    if ac["status"] != "idle" and not kwargs.get("force"):
        logger.error("Aircraft is enroute, use --force flag to ignore")

    ac["status"] = "idle"
    ac["goto"]["x"] = ac["pos"]["x"]
    ac["goto"]["z"] = ac["pos"]["z"]
    ac["goto"]["y"] = -999  # force a landing
    logger.ok("Aircraft is landing")

@ShellEventBus.on("ac.list")
@Helper.command("ac.list", "list all aircrafts", "ac.list")
def list_ac(*args, **kwargs):
    for ac in Aircrafts:
        sess = f"session={ac['session']}" if ac["session"] else "no session"
        logger.info(f"{ac['id']} - {ac['status']} [{sess}] - X: {ac['pos']['x']}, Y: {ac['pos']['y']}, Z: {ac['pos']['z']}")

@ShellEventBus.on("ac.sessions")
@Helper.command("ac.sessions", "list all active flight sessions", "ac.sessions")
def list_sessions(*args, **kwargs):
    if not FlightSessions:
        logger.info("No active sessions")
        return
    for sid, sess in FlightSessions.items():
        logger.info(f"{sid} - {sess['status']} - aircraft={sess['aircraft']}")