# SETTING UP MESSEGES


import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

my_message = [
    SystemMessage(content="You are a gen z assistant"),
    HumanMessage(content="tell me a fun fact")
]

response = llm.invoke(my_message)
print(response.content)
