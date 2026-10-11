
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
rag_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="python_notes_search",
    description=(
        "Search the Python study notes to answer "
        "questions about Python concepts."
    ),
)

# 6. Give the tool to the agent
agent = AgentWorkflow.from_tools_or_functions(
    [rag_tool],
    llm=llm,
)

# 7. Run the agent
async def main():
    response = await agent.run(
        "According to my notes, what is inheritance?"
    )

    print("\nAgent response:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
