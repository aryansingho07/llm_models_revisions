from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

@tool
def add_num(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

llm_with_tools = llm.bind_tools([add_num])

messages = [HumanMessage(content="What is the sum of 5 and 2?")]

# Ask model
ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

# Execute tool
tool_call = ai_msg.tool_calls[0]
tool_result = add_num.invoke(tool_call["args"])

# Send tool output back
messages.append(
    ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call["id"]
    )
)

# Final response
final = llm_with_tools.invoke(messages)

print(final.content)