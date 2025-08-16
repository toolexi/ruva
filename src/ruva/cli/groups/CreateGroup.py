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
def init():
    pass


@init.command()
@click.option("--name", required=True, help="Enter Model name to create")
def modeltrainer(name):
    manager.trigger_configs(TrainerStruct(name=name))


@init.command()
@click.option("--name", required=True, help="Enter finetuner name to create")
def modelfinetuner(name):
    manager.trigger_configs(FinetuneStruct(name=name))


@init.command()
@click.option("--name", required=True, help="Enter dataset name to create")
def dataset(name):
    manager.trigger_configs(DatasetStruct(name=name))


@init.command()
@click.option("--name", required=True, help="Enter agent name to create")
def mcpagent(name):
    manager.trigger_configs(AgentStruct(name=name))


@init.command()
@click.option("--name", required=True, help="Enter workflow name to create")
def agenticworkflow(name):
    manager.trigger_configs(AgenticWorkflowStruct(name=name))
