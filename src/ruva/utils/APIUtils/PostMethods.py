from ruva.pydanticModels._workspace import (
    TrainerStruct,
    FinetuneStruct,
    AgentStruct,
    DatasetStruct,
    AgenticWorkflowStruct,
)

# from ruva.utils.ApiHandler import manager_init

from fastapi import APIRouter
from ruva.utils.WorkspaceManager import WorkspaceManager

manager = WorkspaceManager()

# manager = manager_init()

router = APIRouter(tags=["Create Methods"])


@router.post("/create/model")
def modelTrainer(struct: TrainerStruct):
    manager.triggerConfigs(struct)


@router.post("/create/finetune")
def modelFinetuner(struct: FinetuneStruct):
    manager.triggerConfigs(struct)


@router.post("/create/agent")
def createAgent(struct: AgentStruct):
    manager.triggerConfigs(struct)


@router.post("/create/dataset")
def createDataset(struct: DatasetStruct):
    manager.triggerConfigs(struct)


@router.post("/create/workflow")
def createAgenticWorkflow(struct: AgenticWorkflowStruct):
    manager.triggerConfigs(struct)
