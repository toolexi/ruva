import click
import uvicorn
from ruva.utils import ApiHandler

@click.group(help="Functionality exposed via API")
def server():
    pass


@server.command()
def start():
    uvicorn.run("ruva.utils.ApiHandler:app", reload=True)
