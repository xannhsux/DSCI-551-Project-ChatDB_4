from langchain_community.llms import Ollama
import json

llm = Ollama(model="llama3")

def nl_to_mongo_query(question: str) -> dict:
    prompt = f"""
你是 MongoDB 查询助手。
将用户的问题转换成 Mongo 查询(JSON 格式)，不要包含任何解释：
问题：{question}
"""
    response = llm.invoke(prompt)
    try:
        return json.loads(response.strip())
    except Exception as e:
        raise ValueError(f"解析失败：{e}\n原始输出：{response}")