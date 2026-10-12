# LlamaIndex Agents Course - Learning & Practical Implementations

A hands-on learning repository documenting my journey through the **LlamaIndex module of the Hugging Face Agents Course (Unit 2)**. This repository covers LlamaIndex fundamentals, integrations, RAG, tools, agents, multi-agent systems, and event-driven agentic workflows, with practical implementations in Python using VS Code.

The course theory was studied page by page, and the concepts were explored through runnable Python scripts. For LLM inference, the practicals use Hugging Face Inference API where appropriate and Groq with `openai/gpt-oss-120b` for agent experiments.

---

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Environment Setup](#environment-setup)
- [1. Introduction to LlamaIndex](#1-introduction-to-llamaindex)
- [2. Introduction to LlamaHub](#2-introduction-to-llamahub)
- [3. Components and RAG](#3-components-and-rag)
- [4. Using Tools in LlamaIndex](#4-using-tools-in-llamaindex)
- [5. Using Agents in LlamaIndex](#5-using-agents-in-llamaindex)
- [6. Creating Agentic Workflows](#6-creating-agentic-workflows)
- [Practical Implementations](#practical-implementations)
- [Key Concepts and Comparisons](#key-concepts-and-comparisons)
- [Configuration and Environment Variables](#configuration-and-environment-variables)
- [Troubleshooting](#troubleshooting)
- [What I Learned](#what-i-learned)
- [Future Improvements](#future-improvements)
- [Course Resources](#course-resources)

---

## Overview

**LlamaIndex** is a framework for building applications powered by large language models (LLMs), particularly applications that need to work with external data. It provides components for data ingestion, indexing, retrieval, query engines, tools, agents, and event-driven workflows.

The central goal of this project is to understand how these components fit together and how to use them to build practical AI applications.

The learning progression follows this path:

```text
LlamaIndex Fundamentals
          |
          v
     LlamaHub
          |
          v
  Components and RAG
          |
          v
    Tools and Agents
          |
          v
    Multi-Agent Systems
          |
          v
  Agentic Workflows
          |
          v
 State, Events and Routing
```

### What makes this repository useful?

- Explains concepts through small, understandable examples.
- Demonstrates how ordinary Python functions become agent tools.
- Shows how a RAG query engine can be exposed to an agent.
- Explores multiple specialized agents working together.
- Introduces workflow steps, events, loops, and shared state.
- Uses a reusable project environment and environment variables for API credentials.

## Learning Objectives

By completing these lessons and practicals, I explored how to:

- Understand the architecture and main building blocks of LlamaIndex.
- Find and install integrations through LlamaHub.
- Configure an LLM using a provider integration.
- Build a simple RAG pipeline with documents, embeddings, an index, and a query engine.
- Create `FunctionTool` and `QueryEngineTool` tools.
- Understand ToolSpecs, MCP integrations, and utility tools.
- Initialize agents using `AgentWorkflow` and `ReActAgent`.
- Create single-agent and multi-agent applications.
- Share context and workflow state.
- Build event-driven workflows with multiple steps.
- Implement workflow loops and branching.
- Track tool execution through a shared counter.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| LlamaIndex | Framework for data-centric LLM applications, agents, and workflows |
| LlamaHub | Registry and ecosystem of integrations and tools |
| Groq API | Hosted LLM inference for the agent practicals |
| `openai/gpt-oss-120b` | Model used in the Groq practicals |
| Hugging Face Inference API | Alternative hosted inference integration |
| `BAAI/bge-small-en-v1.5` | Embedding model used in the RAG practical |
| Sentence Transformers | Support for local embedding-model execution |
| `python-dotenv` | Loading environment variables from a `.env` file |
| VS Code | Development environment |

**Note:** The exact APIs and available models can change between package versions and providers. The scripts use the configuration that was tested during this learning exercise; they may need adjustments when run with a different LlamaIndex version.

---

## Project Structure

The following is the logical structure of the practical repository. It includes the main scripts created during the course; adjust filenames if your local copies differ.

```text
LlamaIndex-course/
│
├── .env
├── .gitignore
├── requirements.txt
│
├── 01_llama_hub_test.py
├── 02_llamaindex_agents.py
├── 03_agentic_rag.py
├── 04_multi_agents.py
├── 05_workflow_basics.py
├── 06_multi_agent_workflow.py
│
└── README.md
```

### Script descriptions

| Script | Purpose |
|---|---|
| `01_llama_hub_test.py` | Tests the Hugging Face LLM integration through LlamaIndex |
| `02_llamaindex_agents.py` | Creates a tool-enabled multiplication agent |
| `03_agentic_rag.py` | Builds a small document index and exposes its query engine as a tool |
| `04_multi_agents.py` | Experiments with calculator and information-lookup agents |
| `05_workflow_basics.py` | Explores workflow steps, events, loops, and context state |
| `06_multi_agent_workflow.py` | Explores a multi-agent workflow with specialized agents and shared state |

Some scripts evolved during the lessons. For example, `05_workflow_basics.py` was reused for multiple workflow experiments rather than representing a separate file for every concept.

---

## Environment Setup

### Prerequisites

- Python installed on your system.
- Visual Studio Code.
- An active Python virtual environment.
- A Groq API key for the Groq-based practicals.
- A Hugging Face access token if you want to run the Hugging Face integration example.

### 1. Create the virtual environment

Open a terminal in the project directory:

```powershell
python -m venv myenv
```

Activate it on Windows PowerShell:

```powershell
.\myenv\Scripts\Activate.ps1
```

If your existing `myenv` environment is already configured, reuse it instead of creating another one.

### 2. Install the dependencies

Install the core packages used throughout the practicals:

```powershell
python -m pip install python-dotenv
python -m pip install llama-index-core
python -m pip install llama-index-llms-groq
python -m pip install llama-index-embeddings-huggingface sentence-transformers
```

For the Hugging Face inference integration:

```powershell
python -m pip install llama-index-llms-huggingface-api
```

If an example uses another integration, install its corresponding package as well.

### 3. Create the environment file

Create a `.env` file in the root directory:

```dotenv
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

Only include the credentials for the providers you intend to use.

Never commit your real API keys to GitHub.

### 4. Configure Git to ignore secrets and generated files

Create a `.gitignore` file:

```gitignore
# Environment variables and secrets
.env

# Virtual environments
myenv/
.venv/
venv/

# Python cache
__pycache__/
*.py[cod]

# Generated workflow visualization
flow.html

# Local environment and editor files
.vscode/
```

### 5. Run a script

For example:

```powershell
python .\02_llamaindex_agents.py
```

To check the installed Python environment:

```powershell
python --version
python -m pip show llama-index-core
python -m pip show llama-index-llms-groq
```

---

## 1. Introduction to LlamaIndex

The first PDF introduced LlamaIndex as a toolkit for creating LLM-powered applications and agents that work with data.

The course focuses on three main areas.

### Components

Components are the building blocks used to create applications. Examples include:

- LLM integrations.
- Embedding models.
- Data readers.
- Indexes and retrievers.
- Query engines.
- Tools and prompts.

### Agents and tools

Agents can make decisions and use available tools to accomplish tasks.

Tools expose specific capabilities, such as executing a Python function, searching documents, or accessing an external service.

### Workflows

Workflows organize execution into manageable steps. They can use events and shared state to control how operations proceed.

### Why LlamaIndex?

The course highlights its data-oriented ecosystem, ready-to-use integrations, document-processing capabilities, and structured workflow system.

LlamaIndex overlaps with other agent frameworks, but it is especially useful to understand its approach to data ingestion, retrieval, and agentic workflows.

---

## 2. Introduction to LlamaHub

LlamaHub is a registry and ecosystem of integrations, tools, readers, and other components that can be used with LlamaIndex.

Instead of implementing every integration yourself, you can discover an existing component and install its associated Python package.

### Example: Hugging Face integration

Install the required packages:

```powershell
python -m pip install llama-index-llms-huggingface-api
```

A simplified example of the integration:

```python
import os
from dotenv import load_dotenv

from llama_index.llms.huggingface_api import (
    HuggingFaceInferenceAPI,
)

load_dotenv()

llm = HuggingFaceInferenceAPI(
    model_name="Qwen/Qwen2.5-Coder-32B-Instruct",
    token=os.getenv("HF_TOKEN"),
    provider="auto",
    temperature=0.7,
    max_tokens=100,
)

response = llm.complete("Hello, how are you?")

print(response)
```

### Understanding the import

```python
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
```

- `llama_index.llms.huggingface_api` is the Python module path.
- `HuggingFaceInferenceAPI` is the class imported from that module.

The class provides an interface for communicating with a model through Hugging Face's inference service.

### Understanding the execution

```text
Python Application
       |
       v
LlamaIndex LLM Integration
       |
       v
Hugging Face Inference API
       |
       v
Hosted Model
       |
       v
Generated Response
```

The model is not automatically running locally. The integration sends requests to the hosted inference service.

### Important distinction

LlamaHub is the integration registry and ecosystem; it is not the inference server itself. Installing a package provides the integration code needed by your application.

---

## 3. Components and RAG

This part of the course introduced the components required to build retrieval-augmented generation applications.

### What is RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with LLM-generated responses.

Instead of relying only on the model's pretrained knowledge, an application retrieves relevant information from a supplied data source and uses it to help answer the question.

### The RAG pipeline

```text
Documents
    |
    v
Loading
    |
    v
Parsing and Chunking
    |
    v
Nodes
    |
    v
Indexing and Embeddings
    |
    v
Storage
    |
    v
Retrieval
    |
    v
LLM Generates an Answer
```

The course covers the major stages of loading, indexing, storing, and querying.

### Important components

**Documents:** Represent source data loaded into the application.

**Nodes:** Smaller units of content created from documents for indexing and retrieval.

**Embedding models:** Convert text into numerical vector representations.

**Indexes:** Organize data to support retrieval.

**QueryEngine:** Uses retrieval and response generation to answer questions.

**Evaluation and observability:** Help assess system performance and understand how components behave.

### Practical: Build a small RAG system

The `03_agentic_rag.py` example uses a small collection of Python study notes.

```python
from llama_index.core import Document, VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

documents = [
    Document(
        text=(
            "Python supports inheritance. "
            "Inheritance allows a class to reuse "
            "attributes and methods from another class."
        )
    ),
    Document(
        text="Python lists are ordered and mutable."
    ),
    Document(
        text="A Python dictionary stores key-value pairs."
    ),
]

embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
)
```

This creates an in-memory vector index from the supplied documents.

A query engine can then be created:

```python
query_engine = index.as_query_engine(
    llm=llm,
    similarity_top_k=2,
)
```

Here, `similarity_top_k=2` requests the two most similar retrieved nodes for a query.

The exact answer depends on the source documents, retrieval results, model, and configuration.

### LlamaTrace and observability

The course also introduces observability as a way to inspect application execution and understand component behaviour.

Tracing is particularly useful when an application contains multiple retrieval stages, tools, or agents.

LlamaTrace-related setup may require an Arize Phoenix account, credentials, and compatible configuration. It is an additional observability step rather than a requirement for the basic RAG examples.

---

## 4. Using Tools in LlamaIndex

Tools allow an agent to use capabilities beyond ordinary text generation.

The course introduces four main categories.

### 4.1 FunctionTool

`FunctionTool` wraps a Python function so an agent can use it.

```python
from llama_index.core.tools import FunctionTool

def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b

multiply_tool = FunctionTool.from_defaults(multiply)
```

The function remains ordinary Python code. `FunctionTool` exposes it through LlamaIndex's tool interface.

Tool names and descriptions help the LLM understand when and how to use the tool.

### 4.2 QueryEngineTool

`QueryEngineTool` exposes an existing QueryEngine as a tool.

```python
from llama_index.core.tools import QueryEngineTool

query_engine_tool = QueryEngineTool.from_defaults(
    query_engine,
    name="python_notes_search",
    description=(
        "Search the Python study notes to answer "
        "questions about Python concepts."
    ),
)
```

This lets an agent use an existing RAG query engine rather than implementing the retrieval pipeline inside the agent itself.

### 4.3 ToolSpecs

A ToolSpec groups related tools into a collection. The course uses examples of community-created integrations, including Google-related tools.

The resulting tools can be obtained through the ToolSpec's supported API and then supplied to an agent.

### 4.4 MCP integrations

The course introduces the Model Context Protocol (MCP), a protocol for exposing tools and context to compatible applications.

LlamaIndex can connect to MCP servers through an MCP client and expose available tools to an agent.

An MCP client alone does not create the server; the target server must be configured and running.

### 4.5 Utility tools

The course discusses two utilities for handling data returned by other tools.

**`OnDemandToolLoader`**

Combines loading data, indexing it, and querying the index into one tool call.

**`LoadAndSearchToolSpec`**

Provides separate loading and searching tools. The loading tool executes an existing tool and indexes its output; the search tool queries that index.

These utilities are useful when an agent needs to search or process a large amount of returned information.

---

## 5. Using Agents in LlamaIndex

This section moves from individual tools to agents that can decide how to use them.

### What is an agent?

An agent uses an LLM to interpret a request, choose available actions or tools, process their results, and formulate a response.

For example, an agent could receive a multiplication request and decide to call a Python multiplication function.

### Agent types covered

**Function Calling Agents**

Use models that support function calling to select tools and provide arguments.

**ReAct Agents**

Use a reasoning-and-action loop to determine what to do next, observe tool results, and continue until a response can be produced.

**Advanced Custom Agents**

Support more sophisticated agent behaviour and task coordination.

### Practical: Single-agent tool calling

The `02_llamaindex_agents.py` script demonstrates a multiplication agent using Groq.

```python
import os
import asyncio
from dotenv import load_dotenv

from llama_index.llms.groq import Groq
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool

load_dotenv()

def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    print(f"Tool executed: multiply({a}, {b})")
    return a * b

llm = Groq(
    model="openai/gpt-oss-120b",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=200,
)

multiply_tool = FunctionTool.from_defaults(multiply)

agent = AgentWorkflow.from_tools_or_functions(
    [multiply_tool],
    llm=llm,
)

async def main():
    response = await agent.run(
        "What is 2 times 2? Use the multiplication tool."
    )
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
```

The practical successfully demonstrated the following sequence:

1. The user asks for multiplication.
2. The agent selects the tool and supplies its arguments.
3. Python executes the multiplication.
4. The result is returned to the agent.
5. The agent generates the final response.

The printed message from the Python function verifies that the tool executed.

### Context and agent state

The course introduces `Context` as a mechanism for maintaining workflow state across interactions.

```python
from llama_index.core.workflow import Context

ctx = Context(agent)
```

Reusing the context across runs can maintain state between interactions in the same workflow context.

```python
response1 = await agent.run(
    "My name is Bob.",
    ctx=ctx,
)

response2 = await agent.run(
    "What was my name again?",
    ctx=ctx,
)
```

This illustrates the intended usage, but successful recall depends on the agent's context and memory behaviour. Workflow state should not be confused with permanent storage in a database.

### Practical: Multi-agent systems

The course also demonstrates multiple specialized agents.

The repository's `04_multi_agents.py` experiment includes:

- A calculator agent with addition and subtraction functions.
- An information-lookup agent with access to a QueryEngine tool.
- An `AgentWorkflow` that registers both agents and specifies a root agent.

The calculator tool was verified to execute successfully:

```text
Addition tool called: 125 + 275

Final response:
125 + 275 = 400
```

This confirms that the Python addition function was called and returned the expected result.

A separate RAG request can be used to test whether the information-lookup agent is selected and whether the query tool actually runs.

---

## 6. Creating Agentic Workflows

The final major PDF explores how to organize agent execution into workflows using steps, events, and shared state.

### 6.1 What is a workflow?

A workflow organizes execution into manageable steps. Events communicate data and determine which steps can execute next.

Unlike an ordinary function that directly returns a value, a workflow can coordinate multiple operations and control how they connect.

### 6.2 Workflow components

| Component | Purpose |
|---|---|
| `Workflow` | Base class for a custom workflow |
| `@step` | Marks a method as a workflow step |
| `StartEvent` | Represents the workflow's starting event |
| `StopEvent` | Signals completion and carries the final result |
| Custom `Event` | Carries intermediate information between steps |
| `Context` | Provides access to workflow state |
| `ctx.store.set()` | Stores a value in workflow state |
| `ctx.store.get()` | Retrieves a value from workflow state |

### 6.3 A basic workflow

```python
import asyncio

from llama_index.core.workflow import (
    StartEvent,
    StopEvent,
    Workflow,
    step,
)

class MyWorkflow(Workflow):

    @step
    async def my_step(
        self,
        ev: StartEvent,
    ) -> StopEvent:

        result = "Hello, world!"

        return StopEvent(result=result)

async def main():
    workflow = MyWorkflow(timeout=10)
    result = await workflow.run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

`StopEvent(result="Hello, world!")` creates a stopping event that carries the result. It is not a conditional statement.

When the workflow engine receives the stopping event, the workflow finishes and returns the carried result.

### 6.4 Custom events and multiple steps

A custom event can carry intermediate results from one step to another.

```python
from llama_index.core.workflow import Event

class ProcessingEvent(Event):
    intermediate_result: str
```

A step can return this event to continue the workflow rather than stopping immediately.

For example:

```text
StartEvent
    |
    v
  step_one()
    |
    v
ProcessingEvent
    |
    v
  step_two()
    |
    v
 StopEvent
```

Type annotations help LlamaIndex identify how event types connect steps.

### 6.5 Loops and branching

A workflow can return different event types based on the result of an operation.

For example:

- Return `LoopEvent` to route back to a step that accepts that event.
- Return `ProcessingEvent` to proceed to a later step.
- Return `StopEvent` to finish the workflow.

This pattern can support retries and conditional processing. Production implementations should include appropriate retry limits and error handling.

### 6.6 Drawing workflows

The course introduces `draw_all_possible_flows` to visualize the possible paths through a workflow.

```python
from llama_index.utils.workflow import draw_all_possible_flows

draw_all_possible_flows(workflow, "flow.html")
```

The utility can generate an HTML visualization of the workflow's possible execution paths. Availability and additional dependencies depend on the installed LlamaIndex version.

### 6.7 State management

Workflow state allows different steps to read and update shared information.

For example:

```python
await ctx.store.set("query", "What is the capital of France?")

saved_query = await ctx.store.get("query")
```

The state store holds the value under the key `"query"`.

State is useful when multiple steps need access to information such as:

- The original user request.
- Retrieved information.
- Current processing status.
- Tool-call counters.
- Intermediate results.

State is not automatically permanent. Persistence across application restarts requires an appropriate persistence mechanism.

### 6.8 AgentWorkflow and multi-agent workflows

The course also shows that multi-agent systems can be organized using `AgentWorkflow`.

```python
workflow = AgentWorkflow(
    agents=[multiply_agent, addition_agent],
    root_agent="multiply_agent",
)
```

The root agent receives the initial request. Agents may handle it directly, use their tools, hand off to another agent, or return a response.

The workflow can also receive an initial state and a state prompt:

```python
workflow = AgentWorkflow(
    agents=[multiply_agent, addition_agent],
    root_agent="multiply_agent",
    initial_state={"num_fn_calls": 0},
    state_prompt="Current state: {state}. User message: {msg}",
)
```

A tool can receive the workflow `Context` and update shared state. For example, incrementing `num_fn_calls` each time a tool executes provides a simple way to track tool usage.

The state prompt supplies state information to the agent's prompt context; it does not itself execute tools or guarantee a handoff.

---

## Practical Implementations

The following practicals represent the main hands-on exercises completed during the module.

| Practical | Concepts demonstrated |
|---|---|
| Hugging Face integration test | Provider integration, model configuration, API credentials |
| Multiplication agent | `FunctionTool`, `AgentWorkflow`, tool execution |
| Agentic RAG | Documents, embeddings, index, QueryEngine, `QueryEngineTool` |
| Multi-agent experiment | Specialized agents, calculator tools, RAG lookup |
| Workflow basics | `Workflow`, `@step`, `StartEvent`, `StopEvent` |
| Multi-step workflow | Custom events and intermediate results |
| Looping workflow | Event routing and repeated steps |
| State management | `Context`, `ctx.store.set()`, `ctx.store.get()` |
| Multi-agent workflow | Root agent, specialized agents, shared state |

The exercises were intentionally kept small to focus on the concepts rather than build one large application immediately.

---

## Key Concepts and Comparisons

### FunctionTool vs. QueryEngineTool

| Feature | FunctionTool | QueryEngineTool |
|---|---|---|
| Wraps | Python function | QueryEngine |
| Typical use | Calculations or custom operations | Search and answer questions over data |
| Example | `multiply(5, 3)` | Search Python notes for inheritance |

### Agent vs. Workflow

| Agent | Workflow |
|---|---|
| Uses an LLM to choose actions and tools | Coordinates steps and event-driven transitions |
| Can decide how to approach a task | Can provide explicit control over execution |
| Can operate independently or as part of a workflow | Can include agents as part of its execution |

### `AgentWorkflow` vs. custom `Workflow`

| `AgentWorkflow` | Custom `Workflow` |
|---|---|
| Coordinates one or more agents | Defines custom steps and event routing |
| Supports specialized agents and handoffs | Supports explicit branching, loops, and state |
| Useful for collaborative agent systems | Useful for more controlled application logic |

These approaches are complementary, not mutually exclusive.

### `StartEvent` vs. `StopEvent`

- `StartEvent` represents the starting event.
- `StopEvent` represents completion and carries the final result.

Neither event is a conditional statement.

### State vs. permanent memory

Workflow state is information available during workflow execution. It should not automatically be treated as permanent memory or database storage.

### LlamaHub vs. LlamaIndex

- **LlamaIndex** is the framework used to construct data-centric LLM applications, agents, and workflows.
- **LlamaHub** is the registry and ecosystem for discovering integrations and tools used with LlamaIndex.

---

## Configuration and Environment Variables

### Recommended configuration

Keep provider credentials in `.env`:

```dotenv
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

Load them in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
hf_token = os.getenv("HF_TOKEN")
```

Avoid printing API keys or including them in source code.

### Provider flexibility

The practicals demonstrate that the agent's tools and workflow structure can often remain the same when changing the LLM provider.

For example, switching from Hugging Face to Groq required changing the LLM import and configuration, while the multiplication function and tool setup remained conceptually unchanged.

Provider compatibility, model capabilities, rate limits, token limits, and supported tool-calling mechanisms still need to be checked for the chosen model.

---

## Troubleshooting

### 1. Hugging Face quota or inference errors

**Possible cause:** The selected provider or model has reached a usage limit, or the service is temporarily unavailable.

**What to do:**
- Check the Hugging Face account's current inference availability and limits.
- Verify that the selected model is available through the configured provider.
- Use another supported provider, such as Groq, if appropriate.

### 2. Missing API key

**Possible cause:** `.env` is missing, the key name is incorrect, or the application is running from an unexpected working directory.

**What to do:**

```python
load_dotenv()
print(os.getenv("GROQ_API_KEY") is not None)
```

This checks whether the variable is available without printing the secret itself.

### 3. Tool returns the correct answer but no tool message appears

**Possible cause:** The LLM may have answered directly instead of calling the registered function.

**What to do:**
- Add a print statement inside the Python function.
- Explicitly instruct the agent to use the tool.
- Inspect workflow events or tracing when available.

A correct final answer alone does not prove that a tool was executed.

### 4. `ModuleNotFoundError`

**Possible cause:** The dependency is missing from the active Python environment.

**What to do:**

```powershell
python -m pip install package-name
```

Replace `package-name` with the missing package. Confirm that the correct virtual environment is active.

### 5. Embedding model takes time to load

**Possible cause:** The embedding model is being downloaded or initialized for the first time.

**What to do:**
- Allow the initial download to finish.
- Check network connectivity.
- Confirm the embedding package is installed.

### 6. Workflow loops repeatedly

**Possible cause:** A loop event is repeatedly emitted without a success path.

**What to do:**
- Add a retry counter.
- Set a maximum retry limit.
- Return an error or stopping event when the limit is reached.

### 7. Multi-agent handoff does not happen

**Possible cause:** The root agent may handle the request itself, or the model may not choose the intended handoff.

**What to do:**
- Improve agent descriptions and system prompts.
- Make tool responsibilities distinct.
- Inspect tool execution rather than judging only the final answer.
- Verify that the installed LlamaIndex API supports the configuration being used.

---

## What I Learned

Completing this module helped me understand the architecture of an agentic application beyond simply sending prompts to an LLM.

The main takeaways are:

1. LlamaIndex provides components for working with data and integrating LLMs.
2. LlamaHub helps discover integrations and reusable tools.
3. RAG uses retrieval to ground answers in supplied documents.
4. Tools let agents execute Python functions or access existing query engines.
5. Agents can use specialized tools to accomplish tasks.
6. Multi-agent workflows can divide responsibilities across specialized agents.
7. Custom workflows provide explicit control over execution through steps and events.
8. `Context` and state stores allow workflow components to share information.
9. Tool execution should be verified instead of assuming it occurred because the answer was correct.
10. API credentials and provider configurations should be managed separately from application logic.

The most important lesson is that **reliable agentic applications require more than a capable LLM: they also need well-defined tools, clear execution flow, appropriate state management, and ways to observe what actually happened.**

---

## Future Improvements

Possible extensions to this learning repository include:

- Add unit tests for the Python tools.
- Add error handling and bounded retries to workflows.
- Add structured logging and observability.
- Persist workflow state where required.
- Replace the in-memory RAG index with a persistent vector store.
- Add document loading from PDFs and directories.
- Compare model behaviour across different supported providers.
- Add tool-execution tests for the multi-agent workflow.
- Build a small end-to-end application combining RAG, tools, agents, and workflows.
- Pin working package versions in `requirements.txt` after validating the environment.

These are future improvements, not claims that every item has already been implemented.

---

## Course Resources

The material was based on the LlamaIndex module of the Hugging Face Agents Course.

- [Introduction to LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/introduction)
- [Introduction to LlamaHub](https://huggingface.co/learn/agents-course/unit2/llama-index/llamahub)
- [What Are Components in LlamaIndex?](https://huggingface.co/learn/agents-course/unit2/llama-index/components)
- [Using Tools in LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/tools)
- [Using Agents in LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/agents)
- [Creating Agentic Workflows in LlamaIndex](https://huggingface.co/learn/agents-course/unit2/llama-index/workflows)
- [Quick Self-Check](https://huggingface.co/learn/agents-course/unit2/llama-index/quiz2)
- [Small Quiz](https://huggingface.co/learn/agents-course/unit2/llama-index/quiz1)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)

---

## Acknowledgements

Thanks to the Hugging Face Agents Course and LlamaIndex documentation for providing the learning material and examples.

This repository documents my learning process and practical experiments. It is intended for educational purposes; API behaviour and code compatibility may vary across software versions.

**Status:** LlamaIndex course theory reviewed and core practical concepts explored in VS Code.

**Next learning step:** Continue with the LangGraph module of the Hugging Face Agents Course.
