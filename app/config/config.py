import logging


class Config:
    LOGS_FILE = 'logs/workers.json'
    REGISTRY_FILES_FOLDER = 'registry'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017
    MONGODB_DB = 'admin'
    POSTGRES_HOST = 'postgres'
    POSTGRES_PORT = 5432
    POSTGRES_USER = 'root'
    POSTGRES_PASSWORD = 'root'
    POSTGRES_DATABASE = 'postgres'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = '/app/logs/error.log'
    LOGGING_LEVEL = logging.ERROR
