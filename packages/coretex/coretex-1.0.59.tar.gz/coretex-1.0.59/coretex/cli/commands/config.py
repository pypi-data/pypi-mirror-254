from dataclasses import dataclass
from pathlib import Path

from tabulate import tabulate

import click

from ..modules.utils import arrowPrompt, isGPUAvailable, onBeforeCommandExecute, initializeUserSession
from ..modules.update import dumpScript, UPDATE_SCRIPT_NAME
from ...networking import networkManager
from ...statistics import getAvailableRamMemory
from ...configuration import loadConfig, saveConfig, isUserConfigured, isNodeConfigured, CONFIG_DIR


@dataclass
class LoginInfo:

    username: str
    password: str
    token: str
    tokenExpirationDate: str
    refreshToken: str
    refreshTokenExpirationDate: str


def authenticate(retryCount: int = 0) -> LoginInfo:
    if retryCount >= 3:
        raise Exception("Failed to authenticate. Terminating...")

    username = click.prompt("Email", type = str)
    password = click.prompt("Password", type = str, hide_input = True)

    response = networkManager.authenticate(username, password, False)

    if response.hasFailed():
        click.echo("Failed to authenticate. Please try again...")
        return authenticate(retryCount + 1)

    jsonResponse = response.getJson(dict)

    return LoginInfo(
        username,
        password,
        jsonResponse["token"],
        jsonResponse["expires_on"],
        jsonResponse["refresh_token"],
        jsonResponse["refresh_expires_on"]
    )


def registerNode(name: str) -> str:
    params = {
        "machine_name": name
    }
    response = networkManager.post("service", params)

    if response.hasFailed():
        raise Exception("Failed to configure node. Please try again...")

    accessToken = response.getJson(dict).get("access_token")

    if not isinstance(accessToken, str):
        raise TypeError("Something went wrong. Please try again...")

    return accessToken


def configUser() -> None:
    config = loadConfig()
    if isUserConfigured(config):
        headers = ["username", "server", "storage path"]

        click.echo(click.style("Current Configuration:", fg = "blue"))
        click.echo(tabulate([[
            config["username"],
            config["serverUrl"],
            config["storagePath"]
        ]], headers = headers))

        if not click.prompt(
            "User configuration already exists. Would you like to update (Y/n)?",
            type = bool,
            default = True,
            show_default = False
        ):
            return

    click.echo("Configuring user...")
    loginInfo = authenticate()

    storagePath = click.prompt("Storage path (press enter to use default)", Path.home() / ".coretex", type = str)

    config["username"] = loginInfo.username
    config["password"] = loginInfo.password
    config["token"] = loginInfo.token
    config["refreshToken"] = loginInfo.refreshToken
    config["storagePath"] = storagePath
    config["tokenExpirationDate"] = loginInfo.tokenExpirationDate
    config["refreshTokenExpirationDate"] = loginInfo.refreshTokenExpirationDate

    saveConfig(config)

    click.echo("User successfuly configured")


def configNode() -> None:
    config = loadConfig()
    if not isUserConfigured(config):
        click.echo("User not configured. Run \"coretex config --user\"", err = True)
        return

    if isNodeConfigured(config):
        headers = ["node name", "server", "storage path", "node image"]

        click.echo(click.style("Current Configuration:", fg = "blue"))
        click.echo(tabulate([[
            config["nodeName"],
            config["serverUrl"],
            config["storagePath"],
            config["image"]
        ]], headers = headers))

        if not click.prompt(
            "Node configuration already exists. Would you like to update (Y/n)?",
            type = bool,
            default = True,
            show_default = False
        ):
            return

    click.echo("[Setting up coretex environment]")
    click.echo("[Node Configuration]")

    nodeName = click.prompt("Node name", type = str)
    nodeAccessToken = registerNode(nodeName)

    storagePath = click.prompt("Storage path (press enter to use default)", Path.home() / ".coretex", type = str)

    if isGPUAvailable():
        image = arrowPrompt(["gpu", "cpu"])
    else:
        click.echo("NVIDIA GPU not found, CPU image will be used.")
        image = "cpu"

    ram = click.prompt("Node RAM memory limit in GB (press enter to use default)", type = int, default = getAvailableRamMemory())
    swap = click.prompt("Node swap memory limit in GB, make sure it is larger then mem limit (press enter to use default)", type = int, default = getAvailableRamMemory() * 2)
    sharedMemory = click.prompt("Node POSIX shared memory limit in GB (press enter to use default)", type = int, default = 2)

    config["storagePath"] = storagePath
    config["nodeName"] = nodeName
    config["image"] = image
    config["nodeAccessToken"] = nodeAccessToken
    config["nodeRam"] = ram
    config["nodeSwap"] = swap
    config["nodeSharedMemory"] = sharedMemory

    saveConfig(config)

    # updating node autoupdate script since configuration is changed
    dumpScript(CONFIG_DIR / UPDATE_SCRIPT_NAME, config)

    click.echo("[Node Setup Done] Type \"coretex --help\" for additional information")
    click.echo("For additional help visit our documentation at https://docs.coretex.ai/v1/advanced/coretex-cli/troubleshooting")


@click.command()
@click.option("--user", is_flag = True, help = "Configure user settings")
@click.option("--node", is_flag = True, help = "Configure node settings")
@onBeforeCommandExecute(initializeUserSession, excludeOptions = ["user"])
def config(user: bool, node: bool) -> None:
    if not user and not node:
        raise click.UsageError("Please use either --user or --node")

    if user:
        configUser()

    if node:
        configNode()
