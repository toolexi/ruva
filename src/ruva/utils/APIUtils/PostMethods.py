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


@router.post("/init/model")
def modelTrainer(struct: TrainerStruct):
    manager.trigger_configs(struct)


@router.post("/init/finetune")
def modelFinetuner(struct: FinetuneStruct):
    manager.trigger_configs(struct)


@router.post("/init/agent")
def createAgent(struct: AgentStruct):
    manager.trigger_configs(struct)


@router.post("/init/dataset")
def createDataset(struct: DatasetStruct):
    manager.trigger_configs(struct)


@router.post("/init/workflow")
def createAgenticWorkflow(struct: AgenticWorkflowStruct):
    manager.trigger_configs(struct)
