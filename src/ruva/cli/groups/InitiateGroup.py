import click


@click.group(help=" process triggers")
def initiate():
    pass


@initiate.command()
def training():
    print("training initiated")
