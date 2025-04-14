from fastapi import FastAPI, Query
from .mongo_agent import nl_to_mongo_query
from .sql_agent import answer_sql_question
from .db_config import mongo_col

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM Data Agent API"}

@app.get("/ask/mongo")
def ask_mongo(q: str = Query(...)):
    try:
        query = nl_to_mongo_query(q)
        result = list(mongo_col.find(query, {"_id": 0}))
        return {"query": query, "results": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ask/sql")
def ask_sql(q: str = Query(...)):
    try:
        result = answer_sql_question(q)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.get("/ask")
def ask(q: str = Query(...)):
    try:
        if any(keyword in q.lower() for keyword in ["sql", "database", "table", "select", "customers.db"]):
            result = answer_sql_question(q)
            return {"result": result}
        else:
            query = nl_to_mongo_query(q)
            result = list(mongo_col.find(query, {"_id": 0}))
            return {"result": result}
    except Exception as e:
        return {"error": str(e)}