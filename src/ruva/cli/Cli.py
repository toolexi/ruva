import click
from .groups.CreateGroup import init
from .groups.ApiGroup import server
from .groups.InvokeGroup import invoke
from .groups.AddGroup import add


@click.group(help="The AIOps and DataOps CLI")
def ruva():
    pass


ruva.add_command(init)
ruva.add_command(server)
ruva.add_command(invoke)
ruva.add_command(add)


def main() -> None:
    ruva()
