from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text=["what is capital of India?",
      "what is the capital of France?"
      ]
result=embedding.embed_documents(text)
print(result)