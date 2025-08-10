import click
from .groups.CreateGroup import create
from .groups.InitiateGroup import initiate


@click.group(help="The AIOps and DataOps CLI")
def ruva():
    pass


ruva.add_command(create)
ruva.add_command(initiate)


def main() -> None:
    ruva()
