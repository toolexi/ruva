from pydantic import BaseModel


class MCPToolDefs(BaseModel):
    name: str
    description: str = "tool description"
    version: str = "0.0.1"
    contentType: str = "code | text"
    content: str = "Code | prompt to generate code"
    generate: bool = False


class MCPResourceDefs(BaseModel):
    name: str
    description: str = "resource description"
    version: str = "0.0.1"
    contentType: str = "code | text"
    content: str = "Code | prompt to generate resource"
    generate: bool = False


class MCPPromptDefs(BaseModel):
    name: str
    description: str = "prompt description"
    version: str = "0.0.1"
    contentType: str = "text"
    prompt: str = "Enter your prompt here"
