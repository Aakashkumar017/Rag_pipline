from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def model():
    try:
        llm=ChatOpenAI(
        model="openai/gpt-oss-20b",
        base_url="https://api.groq.com/openai/v1",
        api_key=os.getenv("GROQ_API_KEY"))

        return llm

        print("Grok model is sucessfully load")
    except Exception as e:
        print (f"Error : {e}")
