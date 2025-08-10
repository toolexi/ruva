import click


@click.group(help="bundle of creation subcommands")
def create():
    pass


@create.command()
def train():
    print("initiated training")


@create.command()
def finetune():
    print("initiated finetuning")


@create.command()
def synthesize():
    print("initiated data synthesis")
