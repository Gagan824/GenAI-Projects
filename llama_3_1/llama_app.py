from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

import streamlit as st


st.title("Ask me anything")

template = """Question: {question}

Answer: one word answer"""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1")

chain = prompt | model


question = st.chat_input("How may I help you?")
if question: 
    st.write(question)
    st.write(chain.invoke({"question": question}))