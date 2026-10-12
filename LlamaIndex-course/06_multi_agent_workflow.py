import os
import asyncio
from dotenv import load_dotenv
from llama_index.core.workflow import Context

from llama_index.llms.groq import Groq
from llama_index.core.agent.workflow import (
    AgentWorkflow,
    ReActAgent,
)

load_dotenv()

# 1. Define the tools
async def add(
    ctx: Context,
    a: int,
    b: int,
) -> int:
    """Add two integers."""

    state = await ctx.store.get("state")

    state["num_fn_calls"] += 1

    await ctx.store.set("state", state)

    print(f"Addition tool called: {a} + {b}")
    print(f"Total tool calls: {state['num_fn_calls']}")

    return a + b

async def multiply(
    ctx: Context,
    a: int,
    b: int,
) -> int:
    """Multiply two integers."""

    state = await ctx.store.get("state")

    state["num_fn_calls"] += 1

    await ctx.store.set("state", state)

    print(f"Multiplication tool called: {a} * {b}")
    print(f"Total tool calls: {state['num_fn_calls']}")

    return a * b

# 2. Configure the LLM
llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=300,
)


# 3. Create the multiplication agent
multiply_agent = ReActAgent(
    name="multiply_agent",
    description="Multiplies two integers.",
    system_prompt=(
        "You are a multiplication specialist. "
        "Use your multiplication tool for multiplication requests. "
        "If the user asks for addition, hand off to add_agent."
    ),
    tools=[multiply],
    llm=llm,
)


# 4. Create the addition agent
addition_agent = ReActAgent(
    name="add_agent",
    description="Adds two integers.",
    system_prompt=(
        "You are an addition specialist. "
        "Use your addition tool to calculate sums."
    ),
    tools=[add],
    llm=llm,
)


# 5. Create the multi-agent workflow
workflow = AgentWorkflow(
    agents=[multiply_agent, addition_agent],
    root_agent="multiply_agent",
    initial_state={"num_fn_calls": 0},
    state_prompt=(
        "Current state: {state}. "
        "User message: {msg}"
    ),
)

# 6. Run the workflow
async def main():
    response = await workflow.run(
        user_msg="Can you add 5 and 3?"
    )

    print("\nFinal response:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())