from pydantic import BaseModel
import os
from typing import Optional


class ProjectConfigsStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "AI asset master configs"
    version: str = "0.0.1"
    graphRag: str = "false"


class TrainerStruct(BaseModel):
    name: str
    description: Optional[str] = "Model/LLM Training Configs"
    version: Optional[str] = "0.1.0"
    configType: Optional[str] = "Model"


class FinetuneStruct(BaseModel):
    name: str
    description: str = "LLM Finetune Configs"
    version: str = "0.1.0"
    configType: str = "Finetuner"


class AgentStruct(BaseModel):
    name: str
    description: str = "Agentic Config"
    version: str = "0.1.0"
    configType: str = "Agent"


class DatasetStruct(BaseModel):
    name: str
    description: str = "Dataset synthesis Config"
    version: str = "0.1.0"
    configType: str = "Dataset"


class AgenticWorkflowStruct(BaseModel):
    name: str
    description: str = "Agentic Workflow Config"
    version: str = "0.1.0"
    configType: str = "Workflow"


class AssetManager(BaseModel):
    model: BaseModel


class ProjManager(BaseModel):
    project: ProjectConfigsStruct
