
from calculator_agent import agent
from langchain_core.messages import HumanMessage

# Prepare the initial message
human_message = HumanMessage(content="Add 10 and 5. Multiply the output by 10. Divide the output by 15. Subtract the output by 5. And multiply the output by 9")

# Create an instance of the agent (the compiled graph)
my_agent = agent()

# Prepare the initial state
initial_state = {"messages": [human_message]}

# Invoke the agent
result = my_agent.invoke(initial_state)

# Print all messages in the result
for m in result["messages"]:
    m.pretty_print()