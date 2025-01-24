from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from core.tools import LoadPlaceholders
from core.logging import LoggingManager
from events import EventBus

import threading

logger = LoggingManager("Service.Database")

class DatabaseService:
    """
    A class representing a database service.

    Attributes:
        config (ConfigManager): The configuration object for the database service.
        databases (str[]): A dictionary containing the loaded collections.
    """

    def __init__(self, config, databases: list[str] = []):
        self.config = config
        self.client = None
        self.thread = threading.Thread(target=self.connect)

        self.dbs = {
            #"name": collection
        }

        self.databases_to_load = databases

    def start(self):
        self.thread.start()
        logger.info("Connecting to database server")

    def connect(self) -> None:
            """
            Establishes a connection to the MongoDB database.

            Raises:
                Exception: If unable to establish connection to MongoDB.

            Returns:
                None
            """
            try:
                uri = LoadPlaceholders(self.config.get("DATABASE.URI"), self.config)
                self.client = MongoClient(uri, server_api=ServerApi('1'))

                try:
                    self.client.admin.command('ping')
                    logger.success("Database connection established")

                    self.load_databases()
                    EventBus.signal("database.ready", self)

                except Exception as e:
                    EventBus.signal("error", e, "Service.Database", str(e), fatal=True)
                    return

            except Exception as e:
                EventBus.signal("error", e, "Service.Database", "Unable to establish connection to MongoDB", fatal=True)
                return

    def load_databases(self) -> None:
        """
        Loads the specified databases into the service.

        Returns:
            None
        """
        loaded = 0
        failed = 0

        for db in self.databases_to_load:
            if hasattr(self.client, db):
                self.dbs[db] = getattr(self.client, db)
                loaded += 1
            else:
                failed += 1

        logger.info(f"Loaded {loaded} databases, {failed} failed")

    def get_database(self, name: str):
        """
        Retrieves a database from the service.
        
        Args:
            name (str): The name of the database to retrieve.
        
        Returns:
            Database object if found, None otherwise.
        """

        if name in self.dbs:
            return self.dbs[name]

        return None