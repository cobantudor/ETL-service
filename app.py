from flask import Flask
from flask_crontab import Crontab
from worker.orders_worker import OrdersWorker


app = Flask(__name__)
crontab = Crontab(app)


@app.route("/")
def etl():
    return "ETL app!"


@crontab.job(minute="*/5")
def process_data():
    worker = OrdersWorker()
    worker.process()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
