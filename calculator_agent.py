
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI

# Creating our tools for the agent to use
def add(a : int, b: int) -> int:
    """Adds two numbers."""
    return a + b

def subtract(a : int, b: int) -> int:
    """Subtracts the second number from the first."""
    return a - b


def multiply(a : int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

def divide(a : int, b: int) -> int:
    """Divides the first number by the second. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

tools = [ add, subtract, multiply, divide ]


llm= ChatOpenAI(model="gpt-4", temperature=0)
llm_with_tools = llm.bind_tools(tools, parallel_tool_calls=False)



## Let's create a simple node for defining the assistant behaviour.
from langgraph.graph import MessagesState
from langchain_core.messages import SystemMessage

sys_msg = SystemMessage(content= ' You are a helpful assistant tasked with performing arthimetic operations ')

def assistant_node(state: MessagesState):
    return {'messages' : [llm_with_tools.invoke([sys_msg] + state["messages"])]}



## now let's build and compile the graph
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition

def agent():
    builder = StateGraph(MessagesState)
    builder.add_node("assistant", assistant_node)

    builder.add_node("tools", ToolNode(tools, handle_tool_errors=True))

    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant",
        tools_condition
    )

    # IMPORTANT! -> Now the 'tools' node points back to the 'assistant' node, creating a loop
    builder.add_edge("tools", "assistant")
    return builder.compile()













