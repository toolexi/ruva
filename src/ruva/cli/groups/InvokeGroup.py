from ruva.smarty.models.ModelHandler import ModelHandler
import click
import asyncio

model_handler = ModelHandler


@click.group(help="invoke commands")
def invoke():
    pass


@invoke.command()
def model():
    asyncio.run(
        model_handler(
            model_name="llama3.1:8b", prompt="sample python code"
        ).connect_to_model()
    )
