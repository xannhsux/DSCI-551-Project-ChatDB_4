import json
from pymongo import MongoClient
from . import init_sqlite

def init_mongo():
    client = MongoClient("mongodb://mongodb:27017")
    db = client["mydb"]
    col = db["customers"]
    col.delete_many({})
    with open("/data/customers.json") as f:
        col.insert_many(json.load(f))

if __name__ == "__main__":
    init_mongo()
    init_sqlite.init_sql()

