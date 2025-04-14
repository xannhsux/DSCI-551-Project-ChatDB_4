from langchain_community.llms import Ollama
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from .db_config import sql_engine

llm = Ollama(model="llama3")
db = SQLDatabase(engine=sql_engine)
chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

def answer_sql_question(question: str) -> dict:
    return chain.run(question)