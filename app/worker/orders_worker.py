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

            # Start:    2020-02-26 12:10:46.650717
            # End:      2020-02-26 12:10:47.088068
            orders = extractor.extract_orders('orders')
            users = extractor.extract_users('users')

            # Start:    2020-02-26 11:57:02.710865
            # End:      2020-02-26 12:04:18.774367
            aggregation = extractor.extract_aggregated_data('orders', 'users')

            data = transformer.merge_users_and_orders(users, orders)
            loader.load(data)
            file.write(f"Orders worker finished at: {datetime.now()} \n")
