
from langchain.chains import SQLDatabaseChain
from langchain.sql_database import SQLDatabase
from langchain_community.llms.ollama import Ollama

from .db_config import sql_engine

# Initialize the LLM (Ollama model)
llm = Ollama(model="llama3")

# Initialize the database connection
db = SQLDatabase(engine=sql_engine)

# Create the SQLDatabaseChain with the LLM and database
chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

def answer_sql_question(question: str) -> dict:
    return chain.run(question)
