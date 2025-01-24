import flask
import flask_limiter

from core import Config, Database
from core.tools import LoadPlaceholders
from core.logging import LoggingManager

from events import EventBus

from .services.auth import SessionService
from .services.adapter import Reply

App = flask.Flask(Config.get("SERVER.NAME"))
Limiter = flask_limiter.Limiter(
    app = App,
    key_func = lambda: flask.request.remote_addr,
    storage_uri=LoadPlaceholders(Config.get("DATABASE.URI"), Config),
    strategy="fixed-window",
)


logger = LoggingManager("Server.HTTP")

Sessions = SessionService()

class BlueprintLoader:
    def __init__(self, root="/"):
        self.bps = []
        self.root = root

    def new(self, name):
        bp = flask.Blueprint(name, __name__, url_prefix=f"{self.root}/{name}")
        self.bps.append(bp)
        return bp

    def load(self):
        for bp in self.bps:
            App.register_blueprint(bp)
        logger.info(f"Loaded {len(self.bps)} route blueprints")

#routes
BPLoader = BlueprintLoader(root="/api/v2")

v2blog = BPLoader.new("blog")
v2auth = BPLoader.new("auth")

@EventBus.on("http.start")
def on_server_start():
    BPLoader.load()

@EventBus.on("ready")
def on_ready():
    Sessions.sessions = Database.get_database("users").sessions
    logger.ok("Loaded session service")
 
#error handling
@App.errorhandler(404)
def not_found(e):
    return Reply(error="Route not found"), 404

@App.errorhandler(500)
def internal_error(e):
    EventBus.signal("error", e, "Servers.HTTP", "Server failed to handle request")
    return Reply(error="Internal server error"), 500

@App.errorhandler(429)
def ratelimited(e):
    return Reply(
        error="You are being rate limited",
        retry_after=e.retry_after
    ), 429