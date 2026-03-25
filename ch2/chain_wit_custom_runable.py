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


# TASK 5 [Template For Post]

prompt_post = ChatPromptTemplate.from_messages(
    messages = [
        ("system", "you are a social media post generator. "),
        ("human", "create a post for the following text for linkedlin : {text}")
    ]
       
)


# TASK 6 [Generate the POST]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


# TASK 7 [Output Parser]

str_parser = StrOutputParser()


#CHAIN

chain = prompt_template | llm | str_parser | dictionay_maker_runnabel | prompt_post | llm | str_parser


response = chain.invoke("What is the capital of Punjab")



print(response)
 