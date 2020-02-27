import json

from datetime import datetime
from app.config import Config


class Logger:
    def __init__(self, worker_name):
        self.worker_name = worker_name

    def info(self, message):
        log_data = {
            'timestamp': datetime.now().__str__(),
            'level': 'info',
            'worker': self.worker_name,
            'message': message,
        }

        with open(Config.LOGS_FILE, 'a') as file:
            json_string = json.dumps(log_data)
            file.write(f'{json_string}\n')
