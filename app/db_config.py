from pymongo import MongoClient
from sqlalchemy import create_engine

MONGO_URI = "mongodb://mongodb:27017"
SQLITE_PATH = "/data/customers.db"

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client["mydb"]
mongo_col = mongo_db["customers"]

sql_engine = create_engine(f"sqlite:///{SQLITE_PATH}")