import click

from .commands.node import node
from .commands.project import project
from .commands.config import config


@click.group()
def cli() -> None:
    pass


cli.add_command(config)
cli.add_command(project)
cli.add_command(node)
