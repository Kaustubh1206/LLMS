from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser # string parser output 
# Whenever we are using third party we use community 
from langchain_community.llms import Ollama
import streamlit as st 
import os 
from dotenv import load_dotenv 

load_dotenv()

 
# # OPENAI API


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



# ollama LLMs
llm=Ollama(model='llama3.2:3b') #model
output_parser=StrOutputParser() #responsible in getting output
chain=prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))