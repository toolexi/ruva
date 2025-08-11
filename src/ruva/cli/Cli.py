import click
from .groups.CreateGroup import create
from .groups.ApiGroup import server


@click.group(help="The AIOps and DataOps CLI")
def ruva():
    pass


ruva.add_command(create)
ruva.add_command(server)


def main() -> None:
    ruva()
