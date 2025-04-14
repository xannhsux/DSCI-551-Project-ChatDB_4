from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from pymongo import MongoClient
import json

# Initialize FastAPI app
app = FastAPI()

# 1. Initialize LLaMA model (via Ollama)
llm = Ollama(model="llama3")  # Make sure you have 'ollama run llama3' running locally

# 2. SQL database connection (update with your own path or connection string)
# Example for SQLite: sqlite:///path/to/your.db
sql_db = SQLDatabase.from_uri("data/hotel.db")

# 3. MongoDB connection (check your connection string in MongoDB Compass)
# Replace with your own MongoDB Atlas URI if needed
mongo_client = MongoClient("mongodb+srv://flightsdata:dsci551@flightsdata.y57hp.mongodb.net/")
mongo_db = mongo_client["mydb"]
mongo_col = mongo_db["customers"]

# 4. MongoDB query tool: expects a JSON-formatted string as input
def mongo_query_tool(query_json: str):
    try:
        query_dict = json.loads(query_json)
        result = list(mongo_col.find(query_dict))
        return str(result)
    except Exception as e:
        return f"MongoDB query failed: {e}"

# Create SQL tool using LangChain's built-in SQL toolkit
sql_toolkit = SQLDatabaseToolkit(db=sql_db, llm=llm)
sql_tool = Tool.from_function(
    func=sql_toolkit.get_tools()[0].func,
    name="SQLQueryTool",
    description="Use this tool to query structured data from the SQL database using natural language."
)

# Create MongoDB tool as a custom tool
mongo_tool = Tool(
    name="MongoQueryTool",
    func=mongo_query_tool,
    description="Use this tool to query customer information from MongoDB. Input must be a MongoDB-style JSON query. Example: {\"year\": 2023, \"sales\": {\"$gt\": 10000}}"
)

# Initialize LangChain agent with both tools
agent = initialize_agent(
    tools=[sql_tool, mongo_tool],
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# FastAPI route for natural language queries
@app.get("/ask")
def ask(q: str):
    try:
        response = agent.run(q)
        return {"question": q, "result": response}
    except Exception as e:
        return {"question": q, "error": str(e)}


