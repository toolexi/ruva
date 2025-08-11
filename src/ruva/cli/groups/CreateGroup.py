import click
from ruva.pydanticModels._workspace import (
    TrainerStruct,
    FinetuneStruct,
    AgentStruct,
    DatasetStruct,
    AgenticWorkflowStruct,
)
from ruva.utils.WorkspaceManager import WorkspaceManager

manager = WorkspaceManager()


@click.group(help="Project creation commands")
def create():
    pass


@create.command()
def modeltrainer():
    manager.triggerConfigs(TrainerStruct)


@create.command()
def modelfinetuner():
    manager.triggerConfigs(FinetuneStruct)


@create.command()
def datasynthesizer():
    manager.triggerConfigs(DatasetStruct)


@create.command()
def mcpagent():
    manager.triggerConfigs(AgentStruct)


@create.command()
def agenticworkflow():
    manager.triggerConfigs(AgenticWorkflowStruct)
