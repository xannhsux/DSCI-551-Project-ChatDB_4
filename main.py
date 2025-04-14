from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
