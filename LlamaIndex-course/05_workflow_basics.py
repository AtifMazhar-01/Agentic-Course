# 1. Workflow

# import asyncio

# from llama_index.core.workflow import (
#     StartEvent,
#     StopEvent,
#     Workflow,
#     step,
# )


# class MyWorkflow(Workflow):

#     @step
#     async def my_step(self, ev: StartEvent) -> StopEvent:
#         print("Workflow started!")

#         result = "Hello, world!"

#         print("Workflow step completed!")

#         return StopEvent(result=result)


# async def main():
#     workflow = MyWorkflow(timeout=10, verbose=False)

#     result = await workflow.run()

#     print("\nFinal result:")
#     print(result)


# if __name__ == "__main__":
#     asyncio.run(main())

# 2. Customt event

# import asyncio

# from llama_index.core.workflow import (
#     StartEvent,
#     StopEvent,
#     Workflow,
#     Event,
#     step,
# )


# # 1. Create a custom event
# class ProcessingEvent(Event):
#     intermediate_result: str


# # 2. Create a workflow with two steps
# class MultiStepWorkflow(Workflow):

#     @step
#     async def step_one(
#         self, ev: StartEvent
#     ) -> ProcessingEvent:

#         print("Step 1: Processing initial data")

#         return ProcessingEvent(
#             intermediate_result="Step 1 complete"
#         )

#     @step
#     async def step_two(
#         self, ev: ProcessingEvent
#     ) -> StopEvent:

#         print("Step 2: Using the result from Step 1")

#         final_result = (
#             f"Finished processing: {ev.intermediate_result}"
#         )

#         return StopEvent(result=final_result)


# async def main():
#     workflow = MultiStepWorkflow(
#         timeout=10,
#         verbose=False,
#     )

#     result = await workflow.run()

#     print("\nFinal result:")
#     print(result)


# if __name__ == "__main__":
#     asyncio.run(main())

# 3. Loop Event
# import asyncio
# import random

# from llama_index.core.workflow import (
#     StartEvent,
#     StopEvent,
#     Workflow,
#     Event,
#     step,
# )


# class ProcessingEvent(Event):
#     intermediate_result: str


# class LoopEvent(Event):
#     loop_output: str


# class MultiStepWorkflow(Workflow):

#     @step
#     async def step_one(
#         self,
#         ev: StartEvent | LoopEvent
#     ) -> ProcessingEvent | LoopEvent:

#         if isinstance(ev, LoopEvent):
#             print("Retrying Step 1...")
#         else:
#             print("Starting Step 1...")

#         # Simulate an operation that sometimes fails
#         if random.randint(0, 1) == 0:
#             print("Operation failed. Trying again.")

#             return LoopEvent(
#                 loop_output="Back to step one."
#             )

#         print("Operation succeeded.")

#         return ProcessingEvent(
#             intermediate_result="First step complete."
#         )

#     @step
#     async def step_two(
#         self,
#         ev: ProcessingEvent
#     ) -> StopEvent:

#         print("Executing Step 2...")

#         final_result = (
#             f"Finished processing: {ev.intermediate_result}"
#         )

#         return StopEvent(result=final_result)


# async def main():
#     workflow = MultiStepWorkflow(
#         timeout=10,
#         verbose=False,
#     )

#     result = await workflow.run()

#     print("\nFinal result:")
#     print(result)


# if __name__ == "__main__":
#     asyncio.run(main())

# 4. Context

import asyncio

from llama_index.core.workflow import (
    Context,
    StartEvent,
    StopEvent,
    Workflow,
    step,
)


class QuestionWorkflow(Workflow):

    @step
    async def store_question(
        self,
        ctx: Context,
        ev: StartEvent,
    ) -> StopEvent:

        question = "What is the capital of France?"

        # Save the question in shared state
        await ctx.store.set("query", question)

        print("Question saved in workflow state.")

        # Read the question back
        saved_question = await ctx.store.get("query")

        print(f"Stored question: {saved_question}")

        return StopEvent(result=saved_question)


async def main():
    workflow = QuestionWorkflow(
        timeout=10,
        verbose=False,
    )

    result = await workflow.run()

    print("\nFinal result:")
    print(result)


if __name__ == "__main__":
    asyncio.run(main())