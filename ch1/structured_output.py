import os
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import BaseModel

class llm_schema(BaseModel):
    setup: str
    punchline: str

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature = 1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=os.getenv("GEMINI_API_KEY"),
)


response = llm.invoke("tell me a joke. Generate the output in key-value pair format with the following keys: setup, punchline")

print(response.content)