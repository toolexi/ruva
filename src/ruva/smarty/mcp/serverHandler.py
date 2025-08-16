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


class ServerHandler:
    def __init__(self):
        pass

    def generate_tool(self):
        pass

    def generate_resources(self):
        pass

    def generate_prompts(self):
        pass
