import json
import pandas as pd
from pymongo import MongoClient

from app.config import Config


def migrate_data_from_csv():
    client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
    db = client[Config.MONGODB_DB]

    for file in Config.DATA_FILES:
        collection = db[file]
        data = pd.read_csv(Config.DATA_FILES_PATH + Config.DATA_FILES[file])
        payload = json.loads(data.to_json(orient='records'))
        collection.delete_many({})
        collection.insert_many(payload)


if __name__ == '__main__':
    migrate_data_from_csv()
