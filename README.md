# Langchain Models

This project is a small Python workspace for experimenting with LangChain, Google Gemini, Hugging Face models, embeddings, and similarity search.

## What is done in this project

The repository currently includes working examples for:

- Chat model integration with Google Gemini
- Chat model integration with Hugging Face
- Embedding generation with Google Gemini embeddings
- Embedding generation with Hugging Face embeddings
- A simple document similarity example using cosine similarity
- Basic environment variable loading using dotenv
- A small test script for checking PyTorch and GPU availability

## Project structure

- ChatModels/
  - ChatGemini.py: example of using Gemini as a chat model
  - Deepsheek_localy.py: example using a Hugging Face-based chat model
  - Hugg_tiny.py: another Hugging Face chat example

- Emmbedding_Model/
  - Gemini.py: example of generating embeddings with Gemini
  - Local_hugging.py: example of generating embeddings with Hugging Face
  - Project_Similarity.py: compares documents using cosine similarity

- LLMS/
  - llm_gemini.py: simple Gemini LLM example

- requirements.txt: Python dependencies for the project
- test.py: checks PyTorch version and whether CUDA is available

## Technologies used

- Python
- LangChain
- LangChain Google GenAI
- LangChain Hugging Face
- Hugging Face Transformers
- scikit-learn
- NumPy
- Python-dotenv
- PyTorch

## Setup

1. Create and activate a virtual environment
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create a .env file and add your API keys or configuration if required for Gemini/Hugging Face access.

## How to run

You can run any script directly, for example:

```bash
python ChatModels/ChatGemini.py
```

or

```bash
python Emmbedding_Model/Project_Similarity.py
```

## Notes

- Some examples depend on external APIs or model downloads, so internet access and valid credentials may be required.
- The folder name Emmbedding_Model is intentionally kept as it exists in the repository.
- This project is mainly for learning and experimentation with LLMs and embeddings.

## Summary

This project currently demonstrates the basics of:

- connecting to LLM providers
- using chat models
- generating embeddings
- measuring text similarity
- working with LangChain in a simple Python environment
