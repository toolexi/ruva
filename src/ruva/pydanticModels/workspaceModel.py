from pydantic import BaseModel
import os


class TrainerStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Model/LLM Training Configs"
    version: str = "0.1.0"
    configType: str = "Trainer"


class FinetuneStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "LLM Finetune Configs"
    version: str = "0.1.0"
    configType: str = "Finetuner"


class AgentStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Agentic Config"
    version: str = "0.1.0"
    configType: str = "BaseAgent"


class DatasetStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Dataset synthesis Config"
    version: str = "0.1.0"
    configType: str = "Dataset"


class AgenticWorkflowStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Agentic Workflow Config"
    version: str = "0.1.0"
    configType: str = "AgenticWorkflow"
