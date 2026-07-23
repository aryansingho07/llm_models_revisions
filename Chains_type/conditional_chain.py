from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser,
)
from langchain_core.runnables import RunnableBranch, RunnableLambda

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# LLM
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()


class Feedback(BaseModel):
    review: Literal["positive", "negative"] = Field(
        ...,
        description="The sentiment of the feedback."
    )


feedback_parser = PydanticOutputParser(
    pydantic_object=Feedback
)

# Positive prompt
temp1 = PromptTemplate(
    template="""
Give a warm and appreciative response to the following positive feedback.

{text}
""",
    input_variables=["text"],
)

# Negative prompt
temp2 = PromptTemplate(
    template="""
Give a polite, empathetic, and helpful response to the following negative feedback.

{text}
""",
    input_variables=["text"],
)

# Classification prompt
temp0 = PromptTemplate(
    template="""
Classify the following feedback as either "positive" or "negative".

{text}

{format_instructions}
""",
    input_variables=["text"],
    partial_variables={
        "format_instructions": feedback_parser.get_format_instructions()
    },
)

# Classification chain
chain1 = temp0 | model | feedback_parser

# Branching
branch_chain = RunnableBranch(
    (
        lambda x: x.review == "positive",
        temp1 | model | parser,
    ),
    (
        lambda x: x.review == "negative",
        temp2 | model | parser,
    ),
    RunnableLambda(
        lambda _: "I am not sure about the feedback type. Please provide more details."
    ),
)

# Final chain
chain = chain1 | branch_chain

# Invoke
result = chain.invoke(
    {
        "text": "I am confused and not able to focus."
    }
)

print(result)

chain.get_graph().print_ascii()