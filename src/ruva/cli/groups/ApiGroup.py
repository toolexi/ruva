import click
import uvicorn


@click.group(help="Functionality exposed via API")
def server():
    pass


@server.command()
def start():
    uvicorn.run("ruva.utils.ApiHandler:app", reload=True)
