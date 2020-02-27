import logging
from flask import Flask
from flask_crontab import Crontab

from app.worker.orders_worker import OrdersWorker
from app.config import Config


app = Flask(__name__)
crontab = Crontab(app)

# Setup logging
handler = logging.FileHandler(Config.LOGGING_LOCATION)
handler.setLevel(Config.LOGGING_LEVEL)
formatter = logging.Formatter(Config.LOGGING_FORMAT)
handler.setFormatter(formatter)
app.logger.addHandler(handler)


@app.route("/")
def etl():
    return "ETL app!"


@crontab.job(minute="*/5")
def process_data():
    worker = OrdersWorker()
    worker.process()
