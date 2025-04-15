# 尝试其他导入路径
from langchain_community.llms.ollama import Ollama
import json

llm = Ollama(model="llama3")

def nl_to_mongo_query(question: str) -> dict:
    prompt = f"""
You are a MongoDB query assistant.
Convert the user's question into a MongoDB query in pure JSON format.
Do not include any explanation or extra text.
Question: {question}
"""
    response = llm.invoke(prompt)
    try:
        return json.loads(response.strip())
    except Exception as e:
        raise ValueError(f"Parsing failed: {e}\nOriginal output: {response}")