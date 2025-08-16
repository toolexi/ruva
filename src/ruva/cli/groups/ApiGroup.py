import click
import uvicorn
from ruva.utils.ApiHandler import find_free_port


@click.group(help="Functionality exposed via API")
def server():
    pass


@server.command()
def start():
    port = find_free_port(8000)
    print(port)
    uvicorn.run("ruva.utils.ApiHandler:app", host="127.0.0.1", port=port, reload=True)
