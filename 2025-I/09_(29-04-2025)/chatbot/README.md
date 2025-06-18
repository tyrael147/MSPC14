# Ollama Chatbot

This is a simple chatbot web-app created with streamlit and ollama.
The aim is to learn how to communicate with an LLM server, e.g., ollama.

# Usage

* Download ollama from: https://ollama.com/download/windows
* Once downloaded, install all the dependencies from `requirements.txt`
* Now, download an ollama model from using terminal. Let's test two models: Llama 3.1 1b, and tinyllama. This will take some time...
	```bash
	ollama pull tinyllama
	ollama pull llama3.2:1b
	```

* Once installed, run this command:
  ```bash
  streamlit run main.py
  ```
