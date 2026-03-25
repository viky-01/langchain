import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableLambda




# TASK 1 [Prompt]

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful assistant"),
    ("human", "{input}")
])

# TASK 2 [LLM]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)

# TASK 3 [String Parser]

str_parser = StrOutputParser()

# TASK 4 [Custom Runable]

def dictionay_maker(text: str) -> dict:
    return  {"text" : text}

dictionay_maker_runnabel = RunnableLambda(dictionay_maker)
print(dictionay_maker.invoke("hello world"))

# TASK 5 [Template For Post]

prompt_post = PromptTemplate.chatPromptTemplate(
    
)

# chain = prompt_template | llm | str_parser

# response = chain.invoke({"input" : "what is capital of Bihar"})

# print(response)
