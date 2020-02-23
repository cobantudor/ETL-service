from datetime import datetime

from app.config.config import Config
from app.extractor import Extractor
from app.transformer import Transformer
from app.loader import Loader


class OrdersWorker:
    def __init__(self):
        pass

    def process(self):
        extractor = Extractor()
        transformer = Transformer()
        loader = Loader()
        with open(Config.LOGS_FILE, 'a') as file:
            file.write(f"Orders worker started at: {datetime.now()} \n")
            orders = extractor.extract('orders')
            users = extractor.extract('users')
            data = transformer.merge_users_and_orders(users, orders)
            loader.load(data)
            file.write(f"Orders worker finished at: {datetime.now()} \n")
