import click


@click.group(help="Add assets to your project")
def add():
    pass


@add.command()
@click.option("--name", required=True, help="name your prompt for logging")
@click.option(
    "--target",
    required=True,
    help="Add prompt for model/agent/dataset/workflow/finetuner",
)
def prompt():
    pass
