import click


@click.group(help="Ruva CLI - Executable Intelligence CLI")
def ruva():
    pass


def main():
    ruva()  # pylint: disable=no-value-for-parameter
