class Config:
    LOGS_FILE = 'app/logs/workers.txt'
    DATA_FILES_PATH = 'data/'
    DATA_FILES = {
        'orders': 'orders_202002181303.csv',
        'users': 'users_202002181303.csv'
    }
    REGISTRY_FILES_FOLDER = 'registry'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017
    MONGODB_DB = 'admin'
    POSTGRES_HOST = 'postgress'
    POSTGRES_PORT = 5432
    POSTGRES_USER = 'root'
    POSTGRES_PASSWORD = 'root'
    POSTGRES_DATABASE = 'postgress'
