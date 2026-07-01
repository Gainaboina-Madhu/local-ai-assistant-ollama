import os
import numpy as np
import langchain
import langchain_core
import langchain_ollama
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


Task = 'I have basic knowledge on Python I can learn it in 1 month or not'

temp = ChatPromptTemplate(
    [
        ('system', 'Behave like a 30 year experience u have on python now u can guide me how to learn python'),
        ('user', '{input}')
    ]
)

output = StrOutputParser()

ollama_model = ChatOllama(model='gemma3:1b')

reg = temp | ollama_model | output

result = reg.invoke({'input':Task})


print(result)
