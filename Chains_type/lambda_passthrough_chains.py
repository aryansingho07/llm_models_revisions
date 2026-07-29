from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

parser = StrOutputParser()


def count(text: str) -> int:
    return len(text.split())


joke_prompt = PromptTemplate.from_template(
    "Write a joke about {text}."
)

summary_prompt = PromptTemplate.from_template(
    "Summarize this joke:\n\n{text}"
)


# Generate the joke
joke_chain = joke_prompt | model | parser


# Convert the generated joke into the format expected by summary_prompt
summary_chain = (
    RunnableLambda(lambda joke: {"text": joke})
    | summary_prompt
    | model
    | parser
)


# If joke has more than 25 words, summarize it.
# Otherwise, return a custom message.
branch_chain = RunnableBranch(
    (
        lambda joke: count(joke) > 25,
        summary_chain
    ),
    RunnableLambda(
        lambda joke: (
            f"The joke is too short to summarize. "
            f"It has {count(joke)} words.\n\n"
            f"Original joke:\n{joke}"
        )
    )
)


chain = joke_chain | branch_chain


result = chain.invoke({
    "text": "government"
})

print(result)