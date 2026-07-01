import numpy as np
import langchain
import langchain_ollama

from langchain_ollama import ChatOllama


ollama_model = ChatOllama(model='gemma3:1b')

result = ollama_model.invoke('I want to Join MBA in 2026')

#print(result)
print(result.content)

