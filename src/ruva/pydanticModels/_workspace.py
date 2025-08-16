from pydantic import BaseModel
import os
from typing import Optional


class ProjectConfigsStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "AI asset master configs"
    version: str = "0.0.1"
    graphRag: str = "false"
    ollama: bool = True
    huggingface: bool = False


class TrainerStruct(BaseModel):
    name: str
    description: Optional[str] = "Model/LLM Training Configs"
    version: Optional[str] = "0.1.0"
    configType: Optional[str] = "model"


class FinetuneStruct(BaseModel):
    name: str
    description: str = "LLM Finetune Configs"
    version: str = "0.1.0"
    configType: str = "finetuner"


class AgentStruct(BaseModel):
    name: str
    description: str = "Agentic Config"
    version: str = "0.1.0"
    configType: str = "agent"


class DatasetStruct(BaseModel):
    name: str
    description: str = "Dataset synthesis Config"
    version: str = "0.1.0"
    configType: str = "dataset"


class AgenticWorkflowStruct(BaseModel):
    name: str
    description: str = "Agentic Workflow Config"
    version: str = "0.1.0"
    configType: str = "workflow"


class AgentManager(BaseModel):
    agentName: AgentStruct


class ProjManager(BaseModel):
    project: ProjectConfigsStruct
