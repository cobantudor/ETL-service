import os.path
import pickle
from pymongo import MongoClient
from datetime import datetime

from app.config import Config


class Extractor:
    LAST_EXECUTION_TIME_FIELD = 'last_execution_time'

    def __init__(self):
        self.client = MongoClient(Config.MONGODB_HOST, Config.MONGODB_PORT)
        self.db = self.client[Config.MONGODB_DB]

    def extract_users(self, collection_name):
        valid_users_data_filter = {'user_id': {'$ne': 'null'}}

        return self.process_data_collection(collection_name, valid_users_data_filter)

    def extract_orders(self, collection_name):
        valid_orders_data_filter = {'user_id': {'$ne': 'null'}}

        return self.process_data_collection(collection_name, valid_orders_data_filter)

    def process_data_collection(self, collection_name, valid_data_filter):
        current_execution_timestamp = datetime.now().__str__()

        collection = self.db[collection_name]
        collection_registry_path = self.get_collection_registry_path(collection_name)

        if self.exists_collection_registry_file(collection_registry_path):
            collection_registry = self.read_collection_registry(collection_registry_path)
            last_execution_timestamp = collection_registry.get(self.LAST_EXECUTION_TIME_FIELD)
            documents_filter = {
                '$and': [
                    {'updated_at': {'$gt': last_execution_timestamp}},
                    {'updated_at': {'$lte': current_execution_timestamp}}
                ]
            }
        else:
            documents_filter = {'updated_at': {'$lte': current_execution_timestamp}}

        search_filter = {**valid_data_filter, **documents_filter}
        result_cursor = collection.find(search_filter)

        self.update_last_execution_timestamp(collection_registry_path, current_execution_timestamp)

        return result_cursor

    def get_collection_registry_path(self, collection_name):
        return f'{Config.REGISTRY_FILES_FOLDER}/{collection_name}.dict'

    def exists_collection_registry_file(self, collection_registry_path):
        return os.path.isfile(collection_registry_path)

    def read_collection_registry(self, collection_registry_path):
        with open(collection_registry_path, 'rb') as file:
            return pickle.load(file)

    def write_collection_registry(self, collection_registry_path, collection_registry):
        with open(collection_registry_path, 'wb') as file:
            pickle.dump(collection_registry, file)

    def update_last_execution_timestamp(self, collection_registry_path, current_execution_timestamp):
        collection_registry = {
            self.LAST_EXECUTION_TIME_FIELD: current_execution_timestamp
        }
        self.write_collection_registry(collection_registry_path, collection_registry)
