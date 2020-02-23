from pymongo import MongoClient

from app.config.config import Config


class Extractor:
    def __init__(self):
        pass

    def extract(self, collection):
        client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
        db = client[Config.MONGODB_DB]
        collection = db[collection]

        # Implement storing of the last_update_date_time to be able to make less memory consuming query
        return collection.find()
