from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001" , dimension=8)
result=embeddings.embed_query("What is the capital of India?")
print(result)