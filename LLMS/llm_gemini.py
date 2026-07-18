from langchain_google_genai import GoogleGemini
from dotenv import load_dotenv

load_dotenv()
llm=GoogleGemini(model="gemini-2.0-flash")
result=llm.invoke("india capital")
print(result)