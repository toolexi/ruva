import click
from ruva.pydanticModels.workspaceModel import TrainerStruct, FinetuneStruct, AgentStruct, DatasetStruct, AgenticWorkflowStruct
from ruva.utils.WorkspaceManager import WorkspaceManager

manager = WorkspaceManager()

@click.group(help="bundle of creation subcommands")
def create():
    pass


@create.command()
def modeltrainer():
    commandStruct = TrainerStruct()
    manager.InitiateProject(commandStruct.model_dump())


@create.command()
def modelfinetuner():
    commandStruct = FinetuneStruct()
    manager.InitiateProject(commandStruct.model_dump())


@create.command()
def datasynthesizer():
    commandStruct = DatasetStruct()
    manager.InitiateProject(commandStruct.model_dump())

@create.command()
def mcpagent():
    commandStruct = AgentStruct()
    manager.InitiateProject(commandStruct.model_dump())

@create.command()
def agenticworkflow():
    commandStruct = AgenticWorkflowStruct()
    manager.InitiateProject(commandStruct.model_dump())

# create.add_command(train)
# create.add_command(finetune)
# create.add_command(synthesize)
# create.add_command(agent)
