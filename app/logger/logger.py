import json

from datetime import datetime
from app.config import Config


class Logger:
    def __init__(self, worker_name):
        self.worker_name = worker_name

    def write_record(self, log_data_dict):
        with open(Config.LOGS_FILE, 'a') as file:
            json_string = json.dumps(log_data_dict)
            file.write(f'{json_string}\n')

    def info(self, message):
        log_data = {
            'timestamp': datetime.now().__str__(),
            'level': 'info',
            'worker': self.worker_name,
            'message': message,
        }

        self.write_record(log_data)

    def error(self, error):
        log_data = {
            'timestamp': datetime.now().__str__(),
            'level': 'error',
            'worker': self.worker_name,
            'error': error.__str__(),
        }

        self.write_record(log_data)
