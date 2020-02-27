from app.extractor import Extractor
from app.loader import Loader
from app.transformer import Transformer
from app.logger import Logger


class OrdersWorker:
    def __init__(self):
        self.name='orders_worker'
        self.extractor = Extractor(self.name)
        self.transformer = Transformer(self.name)
        self.loader = Loader(self.name)
        self.logger = Logger(self.name)

    def process(self):
        self.logger.info('Started')

        orders = self.extractor.extract_orders('orders')
        self.logger.info(f'Extracted orders: {orders.count()}')

        users = self.extractor.extract_users('users')
        data = self.transformer.merge_users_and_orders(users, orders)

        self.loader.load(data)
        self.logger.info(f'Written records: {len(data)}')

        self.logger.info('Finished')
