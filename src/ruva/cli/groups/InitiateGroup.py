import click
from ruva.pydanticModels.workspaceModel import TrainerStruct
from ruva.utils.WorkspaceManager import WorkspaceManager


@click.group(help=" process triggers")
def initiate():
    pass


@initiate.command()
def training():
    print("training initiated")
    trainerStruct = TrainerStruct()
    w = WorkspaceManager()
    # print(workspaceStruct.model_dump())
    w.InitiateProject(trainerStruct.model_dump())
