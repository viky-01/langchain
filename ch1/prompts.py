# PROMPTS

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from langchain_core.prompts import PromptTemplate

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


# my_message = [
#     SystemMessage(content="You are a gen z assistant"),
#     HumanMessage(content="tell me a fun fact")
# ]

user_input = input("Enter a topic : ")

dynamic_prompt = PromptTemplate.from_template("write a fun fact about {topic}")

ready_prompt = dynamic_prompt.invoke({"topic" : user_input})

response = llm.invoke(ready_prompt)

print(response.content)
