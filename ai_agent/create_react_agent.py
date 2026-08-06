from dotenv import load_dotenv

from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

load_dotenv()

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# Search Tool
@tool
def search_tool(query: str) -> str:
    """Search the web using DuckDuckGo."""
    search = DuckDuckGoSearchResults()
    return search.invoke(query)

# Prompt
prompt = hub.pull("hwchase17/react")

# Agent
agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

# Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

response = agent_executor.invoke(
    {
        "input": "Top news headlines of today"
    }
)

print(response)