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
@click.option("--name", required=True, help="Enter Model name to create")
def modeltrainer(name):
    manager.triggerConfigs(TrainerStruct(name=name))


@create.command()
@click.option("--name", required=True, help="Enter finetuner name to create")
def modelfinetuner(name):
    manager.triggerConfigs(FinetuneStruct(name=name))


@create.command()
@click.option("--name", required=True, help="Enter dataset name to create")
def dataset(name):
    manager.triggerConfigs(DatasetStruct(name=name))


@create.command()
@click.option("--name", required=True, help="Enter agent name to create")
def mcpagent(name):
    manager.triggerConfigs(AgentStruct(name=name))


@create.command()
@click.option("--name", required=True, help="Enter workflow name to create")
def agenticworkflow(name):
    manager.triggerConfigs(AgenticWorkflowStruct(name=name))
