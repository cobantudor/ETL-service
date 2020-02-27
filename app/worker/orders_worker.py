from app.extractor import Extractor
from app.loader import Loader
from app.transformer import Transformer
from app.logger import Logger


class OrdersWorker:
    def __init__(self):
        self.extractor = Extractor()
        self.transformer = Transformer()
        self.loader = Loader()
        self.logger = Logger('Orders worker')

    def process(self):
        self.logger.info('Started')

        orders = self.extractor.extract_orders('orders')
        self.logger.info(f'Extracted orders: {orders.count()}')

        users = self.extractor.extract_users('users')
        self.logger.info(f'Extracted users: {users.count()}')

        data = self.transformer.merge_users_and_orders(users, orders)

        self.loader.load(data)
        self.logger.info(f'Written records: {len(data)}')

        self.logger.info('Finished')
