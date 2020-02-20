from datetime import datetime


class OrdersWorker:
    def __init__(self):
        pass

    def process(self):
        with open('logs/workers.txt', 'a') as file:
            file.write(f"Orders worker started at: {datetime.now()} \n")
