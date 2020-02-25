from datetime import datetime

from app.config import Config
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
            orders = extractor.extract_orders('orders')
            users = extractor.extract_users('users')
            data = transformer.merge_users_and_orders(users, orders)
            loader.load(data)
            file.write(f"Orders worker finished at: {datetime.now()} \n")
