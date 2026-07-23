from langchain_huggingface import ChatHuggingFace ,HuggingFacePipeline
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()


llm = HuggingFacePipeline.from_model_id(
    model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
    task="text-generation",
    pipeline_kwargs={
        "temperature":0.5,
        "max_new_tokens":100,
    },
)
model = ChatHuggingFace(llm=llm)
temp1=PromptTemplate.from_template("write deatiled report on {topic}?")

temp2=PromptTemplate.from_template("sumarise the given text {text}")

parser=StrOutputParser()

chain=temp1 | model | parser | temp2 | model | parser
result=chain.invoke({"topic":"langchain"})
print(result)