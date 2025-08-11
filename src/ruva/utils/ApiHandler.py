from fastapi import FastAPI
from ruva.utils.WorkspaceManager import WorkspaceManager
from ruva.pydanticModels._workspace import (
    TrainerStruct,
    FinetuneStruct,
    AgentStruct,
    DatasetStruct,
    AgenticWorkflowStruct,
)

manager = WorkspaceManager()

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to ruva"

@app.post("/create/trainer")
def createTrainer():
    manager.triggerConfigs(TrainerStruct)
    return "trainer configs created"