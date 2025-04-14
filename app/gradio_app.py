import gradio as gr
import requests
import os
import json

# Get API URL from environment or use default
API_URL = os.environ.get("API_URL", "http://localhost:8000")

def ask_backend(question):
    try:
        response = requests.get(f"{API_URL}/ask", params={"q": question})
        result = response.json()
        
        if "error" in result:
            return f"Error: {result['error']}"
        
        # Format the response nicely
        if "result" in result:
            return result["result"]
        else:
            return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Error connecting to backend: {str(e)}"

with gr.Blocks(title="LLM Data Agent") as demo:
    gr.Markdown("# LLM Data Agent")
    gr.Markdown("Query SQL and MongoDB using natural language with LLaMA")
    
    with gr.Row():
        with gr.Column():
            query_input = gr.Textbox(label="Ask a question to SQL + MongoDB", placeholder="Find customers with name John")
            submit_btn = gr.Button("Submit Query")
        
    with gr.Row():
        output = gr.Textbox(label="Result")
    
    submit_btn.click(fn=ask_backend, inputs=query_input, outputs=output)
    query_input.submit(fn=ask_backend, inputs=query_input, outputs=output)

# Launch with network interface to work in Docker
demo.launch(server_name="0.0.0.0", server_port=7860)