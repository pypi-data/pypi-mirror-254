import asyncio
import os

from dotenv import load_dotenv
from openai import AzureOpenAI, AsyncAzureOpenAI

from parea import Parea
from parea.cookbook.data.openai_input_examples import simple_example, functions_example
from parea.utils.trace_utils import trace

load_dotenv()

client = AzureOpenAI(
    api_version="2023-12-01-preview",
    api_key=os.getenv("AZURE_OAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OAI_DEPLOYMENT")
)
aclient = AsyncAzureOpenAI(
    api_version="2023-12-01-preview",
    api_key=os.getenv("AZURE_OAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OAI_DEPLOYMENT")
)


p = Parea(api_key=os.getenv("PAREA_API_KEY"))
p.wrap_openai_client(client)
p.wrap_openai_client(aclient)


@trace
def call_azure(data: dict):
    response = client.chat.completions.create(**data)
    print(response)


@trace
def call_azure_stream(data: dict):
    data["stream"] = True
    stream = client.chat.completions.create(**data)
    for chunk in stream:
        if chunk.choices:
            print(chunk.choices[0].delta or "")


@trace
async def acall_azure(data: dict):
    response = await aclient.chat.completions.create(**data)
    print(response)


@trace
async def acall_azure_stream(data: dict):
    data["stream"] = True
    stream = await aclient.chat.completions.create(**data)
    async for chunk in stream:
        if chunk.choices:
            print(chunk.choices[0].delta or "")


if __name__ == "__main__":
    call_azure(simple_example)
    # call_azure_stream(simple_example)
    # call_azure_stream(functions_example)
    # asyncio.run(acall_azure(simple_example))
    asyncio.run(acall_azure(functions_example))
    # asyncio.run(acall_azure_stream(simple_example))
    # asyncio.run(acall_azure_stream(functions_example))
