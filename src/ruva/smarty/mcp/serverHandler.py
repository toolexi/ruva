import tomlkit
from pydantic import BaseModel
from typing import Dict

from ruva.pydanticModels._mcp_handlers import MCPToolDefs


class ServerHandler:
    def __init__(self):
        pass

    def manage_configs(self, configs: Dict):

        doc = tomlkit.document()
        return doc

    def generate_tool(self, name: str, struct: BaseModel):
        configs = struct(name=name).model_dump()
        print(configs)
        return configs

    def generate_resources(self, name: str, struct: BaseModel):
        configs = struct(name=name).model_dump()
        return configs

    def generate_prompts(self, name: str, struct: BaseModel):
        configs = struct(name=name).model_dump()
        return configs


if __name__ == "__main__":
    server = ServerHandler()
    server.generate_tool("test", MCPToolDefs)
