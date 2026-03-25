import os
from dotenv import load_dotenv
from google import genai

load_dotenv() 

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="tell me a fun fact in clash of clan",
)

print(response.text)


from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  
    max_tokens=None,
    timeout=None,
    max_retries=2,
   
)

model.invoke("tell em a fun fact")