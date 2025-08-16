from pydantic import BaseModel
import httpx

# import asyncio
import json


class ModelHandlerConfig(BaseModel):
    name: str
    type: str = "text-classification"
    modality: str = "text"
    purpose: str = "generation"


class InputPayload(BaseModel):
    model_name: str
    prompt: str


class HFModelMetadata:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def get_model_info(self):
        pass


class OllamaHandler:
    def __init__(self, input_payload: BaseModel):
        self.input_payload = input_payload.model_dump()

    async def query_model(self):
        async with httpx.AsyncClient(timeout=None) as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/generate",
                json={
                    "model": self.input_payload["model_name"],
                    "prompt": self.input_payload["prompt"],
                },
            ) as response:
                async for line in response.aiter_lines():
                    if line.strip():
                        data = json.loads(line)
                        if "response" in data:
                            print(data["response"], end="", flush=True)
