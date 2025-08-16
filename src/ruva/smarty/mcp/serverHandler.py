# # To load from a file:
# with open("config.toml", "rb") as f:
#     data = tomli.load(f)
# print(data)

# To load from a string:
# toml_string = """
# [database]
# type = "postgresql"
# host = "localhost"
# port = 5432
# """
# data_from_string = tomli.loads(toml_string)
# print(data_from_string)
import tomlkit
from pydantic import BaseModel
from typing import Dict

from ruva.smarty.handlers.MCPHandlers import MCPToolDefs


class ServerHandler:
    def __init__(self):
        pass

    def manage_configs(self, configs: Dict):

        doc = tomlkit.document()
        return doc

    def generate_tool(self, name: str, struct: BaseModel):
        configs = struct(name=name).model_dump()
        print(type(configs))
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
