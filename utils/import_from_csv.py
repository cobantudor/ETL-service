import pandas as pd
from pymongo import MongoClient
import json

data_files = {
    'orders': 'orders_202002181303.csv',
    'users': 'users_202002181303.csv'
}

client = MongoClient('mongo', 27017)
db = client['admin']

for file in data_files:
    coll = db[file]
    data = pd.read_csv('/data/' + data_files[file])
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)
