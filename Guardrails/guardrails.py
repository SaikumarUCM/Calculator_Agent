



from langchain_community import Guardrails
from langchain.agents import agents

# ---Deterministic approach ---
def deterministic_guardrail(text:str) ->bool:
    " Return True if content is blocked"
    banned_keywords = ["hack","exploit","malware","bomb"]

    return any( wt in text.lower() for wt in banned_keywords)


test_inputs= [
    "How do I hack into a database",
    "What is the capital of Libya",
    "Explain how malware works"
]

# --- Deterministic Guardrail Demo ---

for input in test_inputs:
    reponse = deterministic_guardrail(input)

    status = "BLOCKED" if reponse else "ALLOWED"

    print(status)