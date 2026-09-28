from langchain_ollama import ChatOllama
from langchain.agents import create_agent

model = ChatOllama(model="llama3.2:latest")
agent = create_agent(model)
