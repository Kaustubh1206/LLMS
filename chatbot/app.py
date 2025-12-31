from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st 
import os 
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")


# # OPENAI API
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# LANGSMITH TRACKING
# For tracing and monitoring 
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## PROMPT TEMPLATE

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpuful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

#Streamlit 

st.title('Langchain Demo With OpenAI API ')
input_text=st.text_input("Search the topic you want")


# open Ai LLMs
llm=ChatOpenAI(model='gpt-3.5-turbo') #model
output_parser=StrOutputParser() #responsible in getting output
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))