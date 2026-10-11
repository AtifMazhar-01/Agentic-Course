import os
import asyncio
from dotenv import load_dotenv

# from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.llms.groq import Groq
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool

from llama_index.core.workflow import Context

load_dotenv()

# 1. Create a Python function
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    print(f"Tool executed: multiply({a}, {b})")
    return a * b


# 2. Configure the language model
# llm = HuggingFaceInferenceAPI(
#     model_name="Qwen/Qwen2.5-72B-Instruct", # or Qwen/Qwen2.5-Coder-32B-Instruct",
#     token=os.getenv("HF_TOKEN"),
#     provider="auto",
#     max_tokens=200,
# )



llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=200,
)



# 3. Convert the function into a tool
multiply_tool = FunctionTool.from_defaults(multiply)

# 4. Initialize the agent with its tool
agent = AgentWorkflow.from_tools_or_functions(
    [multiply_tool],
    llm=llm,
)

# 5. Run the agent
# async def main():
#     response = await agent.run(
#         "What is 17 multiplied by 23? Use the multiplication tool."
#     )
#     print("\nAgent response:")
#     print(response)


async def main():
    # Create context for this agent
    ctx = Context(agent)

    # First interaction
    response1 = await agent.run(
        "My name is Atif.",
        ctx=ctx
    )
    print("First response:")
    print(response1)

    # Second interaction using the same context
    response2 = await agent.run(
        "What was my name again?",
        ctx=ctx
    )
    print("\nSecond response:")
    print(response2)

if __name__ == "__main__":
    asyncio.run(main())
