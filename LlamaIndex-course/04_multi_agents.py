
from llama_index.core.agent.workflow import (
    AgentWorkflow,
    ReActAgent,
)

import os
import asyncio
from dotenv import load_dotenv

from llama_index.core import Document, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

load_dotenv()

# 1. Create our small knowledge base
documents = [
    Document(
        text="Python supports inheritance. "
             "Inheritance allows a class to reuse "
             "attributes and methods from another class."
    ),
    Document(
        text="Python lists are ordered and mutable. "
             "Lists can store multiple items."
    ),
    Document(
        text="A Python dictionary stores data as "
             "key-value pairs."
    ),
]

# 2. Create embeddings
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# 3. Build an index from our documents
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
)

# 4. Create a QueryEngine
llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=300,
)

query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=2,
)

# 5. Wrap the QueryEngine as a tool
query_engine_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="python_notes_search",
    description=(
        "Search the Python study notes to answer "
        "questions about Python concepts."
    ),
)

# Tool 1: Addition
def add(a: int, b: int) -> int:
    """Add two numbers."""
    print(f"Addition tool called: {a} + {b}")
    return a + b


# Tool 2: Subtraction
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    print(f"Subtraction tool called: {a} - {b}")
    return a - b


# Agent 1: Calculator
calculator_agent = ReActAgent(
    name="calculator",
    description="Performs basic arithmetic operations",
    system_prompt=(
        "You are a calculator assistant. "
        "Use your tools for math operations."
    ),
    tools=[add, subtract],
    llm=llm,
)

# Agent 2: Information lookup
query_agent = ReActAgent(
    name="info_lookup",
    description="Looks up information in Python study notes",
    system_prompt=(
        "Use your query tool to answer questions "
        "about Python concepts from the study notes."
    ),
    tools=[query_engine_tool],
    llm=llm,
)

# Create the multi-agent workflow
agent = AgentWorkflow(
    agents=[calculator_agent, query_agent],
    root_agent="calculator",
)


# async def main():
#     response = await agent.run(
#         user_msg="Can you add 5 and 3?"
#     )

#     print("\nFinal response:")
#     print(response)

async def main():
    response = await agent.run(
        user_msg=(
            "You must use the calculator agent's addition tool "
            "to calculate 125 + 275. Do not calculate mentally."
        )
    )

    print("\nFinal response:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
