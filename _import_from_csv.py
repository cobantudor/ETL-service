import json
import pandas as pd
from pymongo import MongoClient

from app.config import Config


def migrate_data_from_csv():
    data_files_path = 'data/'
    data_files = {
        'orders': 'orders_202002181303.csv',
        'users': 'users_202002181303.csv'
    }

    client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
    db = client[Config.MONGODB_DB]

    for file in data_files:
        collection = db[file]
        data = pd.read_csv(data_files_path + data_files[file])
        payload = json.loads(data.to_json(orient='records'))
        collection.delete_many({})
        collection.insert_many(payload)


if __name__ == '__main__':
    migrate_data_from_csv()
