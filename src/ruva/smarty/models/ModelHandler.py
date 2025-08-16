from ruva.pydanticModels._model_handlers import OllamaHandler, InputPayload


class ModelHandler:
    def __init__(self, model_name: str, prompt: str):
        self.ollama_handler = OllamaHandler
        self.model_payload = InputPayload(model_name=model_name, prompt=prompt)

    async def connect_to_model(self):
        responses = await self.ollama_handler(
            input_payload=self.model_payload
        ).query_model()
        return responses
