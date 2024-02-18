import click

from ..modules import node as node_module
from ..modules.update import NodeStatus, getNodeStatus, activateAutoUpdate
from ..modules.utils import onBeforeCommandExecute
from ..modules.docker import isDockerAvailable
from ...configuration import loadConfig, CONFIG_DIR


@click.command()
def start() -> None:
    config = loadConfig()
    repository = "coretexai/coretex-node"
    tag = f"latest-{config['image']}"

    if node_module.isRunning():
        if not click.prompt(
            "Node is already running. Do you wish to restart the Node? (Y/n)",
            type = bool,
            default = True,
            show_default = False
        ):
            return

        click.echo("Stopping Coretex Node...")
        node_module.stop()
        click.echo("Successfully stopped Coretex Node.")


    if node_module.shouldUpdate(repository, tag):
        click.echo("Fetching latest node version...")
        node_module.pull("coretexai/coretex-node", f"latest-{config['image']}")
        click.echo("Latest node version successfully fetched.")

    click.echo("Starting Coretex Node...")
    node_module.start(f"{repository}:{tag}", config)
    click.echo("Successfully started Coretex Node.")

    activateAutoUpdate(CONFIG_DIR, config)


@click.command()
def stop() -> None:
    if not node_module.isRunning():
        click.echo("Node is already offline.")
        return

    click.echo("Stopping Coretex Node...")
    node_module.stop()
    click.echo("Successfully stopped Coretex Node.")


@click.command()
def update() -> None:
    config = loadConfig()
    repository = "coretexai/coretex-node"
    tag = f"latest-{config['image']}"

    nodeStatus = getNodeStatus()

    if nodeStatus == NodeStatus.inactive:
        click.echo("Node is not running. To update Node you need to start it first.")
        return

    if nodeStatus == NodeStatus.reconnecting:
        click.echo("Node is reconnecting. Cannot update now.")
        return

    if nodeStatus == NodeStatus.busy:
        if not click.prompt("Node is busy, do you wish to terminate the current execution to perform the update? (Y/n)",
            type = bool,
            default = True,
            show_default = False
        ):
            return

        click.echo("Stopping Coretex Node...")
        node_module.stop()
        click.echo("Successfully stopped Coretex Node.")

    if not node_module.shouldUpdate(repository, tag):
        click.echo("Node is already up to date.")
        return

    click.echo("Fetching latest node version.")
    node_module.pull(repository, tag)
    click.echo("Latest version successfully fetched.")

    if getNodeStatus() == NodeStatus.busy:
        if not click.prompt("Node is busy, do you wish to terminate the current execution to perform the update? (Y/n)",
            type = bool,
            default = True,
            show_default = False
        ):
            return

    click.echo("Stopping Coretex Node...")
    node_module.stop()
    click.echo("Successfully stopped Coretex Node.")

    click.echo("Starting Coretex Node...")
    node_module.start(f"{repository}:{tag}", config)
    click.echo("Successfully started Coretex Node.")


@click.group()
@onBeforeCommandExecute(isDockerAvailable)
def node() -> None:
    pass


node.add_command(start, "start")
node.add_command(stop, "stop")
node.add_command(update, "update")
