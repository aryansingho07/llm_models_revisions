from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001", dimension=8)
documents=["aryan is a boy",
           "sneha is a girl",
           "dheeraj is gay",
           "aryan is good boy"
           ]
docu_emb=embeddings.embed_documents(documents)
statement="aryan is a"
state_emb=embeddings.embed_query(statement)
score=cosine_similarity([state_emb],docu_emb)[0]
index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]
print("most similare doc :",documents[index],"score:",score)
