from pydantic import BaseModel
import os

class TrainerStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Model/LLM Training Configs"
    version: str = "0.1.0"

class FinetuneStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "LLM Finetune Configs"
    version: str = "0.1.0"

class AgentStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Agentic config"
    version: str = "0.1.0"

class DatasetStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Dataset synthesis config"
    version: str = "0.1.0"

class AgenticWorkflowStruct(BaseModel):
    name: str = os.path.basename(os.getcwd())
    description: str = "Agentic Workflow"
    version: str = "0.1.0"
