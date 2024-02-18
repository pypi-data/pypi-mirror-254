import typer
import requests
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich import print as console
from typing import Union
from typing_extensions import Annotated, Optional

from cerebrium import api
from cerebrium.core import cli
from cerebrium import utils


def _status_color(status: str) -> str:
    """Takes a status, returns a rich markup string with the correct color"""
    status = " ".join([s.capitalize() for s in status.split("_")])
    color = None
    if status == "Active":
        color = "green"
    elif status == "Cold":
        color = "bright_cyan"
    elif status == "Pending":
        color = "yellow"
    elif status == "Deploying":
        color = "bright_magenta"
    elif "error" in status.lower():
        color = "red"

    if color:
        return f"[bold {color}]{status}[bold /{color}]"
    else:
        return f"[bold]{status}[bold]"


def _pretty_timestamp(timestamp: str) -> str:
    """Converts a timestamp from 2023-11-13T20:57:12.640Z to human readable format"""
    return timestamp.replace("T", " ").replace("Z", "").split(".")[0]


@cli.command()
def apps(
    api_key: Annotated[
        Optional[str], typer.Option("--api-key", "-k", help="API key to use")
    ] = None,
):
    """Lists all apps in your project"""

    # Get the API key
    if api_key is None:
        api_key = utils.get_api_key()

    # Get the apps
    headers = {"Authorization": api_key, "ContentType": "application/json"}
    app_response = requests.get(f"{api.api_url}/get-models", headers=headers)
    api._check_response(app_response, key="models")
    apps = app_response.json()

    apps_to_show = []
    for a in apps["models"]:
        # if isinstance(a, list):
        replicas = a.get("replicas", ["None"])
        replicas = [r for r in replicas if r != ""]
        # convert updatedat from 2023-11-13T20:57:12.640Z to human readable format
        updated_at = _pretty_timestamp(a.get("updatedAt", "None"))

        apps_to_show.append(
            {
                "id": f'{a["projectId"]}-{a["name"]}',
                "status": _status_color(a["status"]),
                "replicas": replicas,
                "updatedAt": updated_at,
            }
        )

    # sort by updated date
    apps_to_show = sorted(apps_to_show, key=lambda k: k["updatedAt"], reverse=True)

    # Create the table
    table = Table(title="", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("ModelId")
    table.add_column("Status")
    table.add_column("Replicas", justify="center")
    table.add_column("Last Updated", justify="center")

    for entry in apps_to_show:
        table.add_row(
            entry["id"],
            entry["status"],
            "\n".join(entry["replicas"]),
            entry["updatedAt"],
        )

    details = Panel.fit(
        table,
        title="[bold] App Details ",
        border_style="yellow bold",
        width=100,
        padding=(1, 1),
    )
    console(details)


@cli.command()
def app(
    app_id: Annotated[
        str,
        typer.Argument(
            help="App ID to get details for. You can get this from `cerebrium get-apps` or from your model dashboard",
        ),
    ],
    api_key: Annotated[
        Optional[str], typer.Option("--api-key", "-k", help="API key for your project")
    ] = None,
):
    """Returns the details of an app. Add a replica ID to get details of a specific replica"""

    if not api_key:
        api_key = utils.get_api_key()

    headers = {"Authorization": api_key, "ContentType": "application/json"}

    app_response = requests.get(
        f"{api.api_url}/get-model-details?modelId={app_id}",
        headers=headers,
    )
    api._check_response(app_response)
    app_response: dict = app_response.json()

    table = make_detail_table(app_response)
    details = Panel.fit(
        table,
        title=f"[bold] App Details for {app_id} [/bold]",
        border_style="yellow bold",
        width=100,
        padding=(1, 1),
    )

    print()
    console(details)
    print()


def make_detail_table(data: dict):
    def get(key):
        return str(data.get(key)) if data.get(key) else "Data Unavailable"

    def addRow(
        leader: str, key: str = "", value=None, ending: str = "", optional=False
    ):
        if value is None:
            if key not in data:
                ending = ""
            if optional:
                if data.get(key):
                    table.add_row(leader, get(key) + ending)
            else:
                table.add_row(leader, get(key) + ending)
        else:
            table.add_row(leader, str(value))

    # Create the tables
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("Parameter", style="")
    table.add_column("Value", style="")
    table.add_row("MODEL", "", style="bold")
    table.add_row("Name", data.get("name"))
    addRow("Average Runtime", "averageModelRunTimeSeconds", ending="s")
    addRow("Cerebrium Version", "cerebriumVersion")
    addRow("Created At", "createdAt", _pretty_timestamp(get("createdAt")))
    if get("createdAt") != get("updatedAt"):
        addRow("Updated At", "updatedAt", _pretty_timestamp(get("updatedAt")))

    table.add_row("", "")
    table.add_row("HARDWARE", "", style="bold")
    table.add_row("GPU", get("hardware"))
    addRow("CPU", "cpu", ending=" cores")
    addRow("Memory", "memory", ending=" GB")
    if get("hardware") != "CPU" and "hardware" in data:
        addRow("GPU Count", "gpuCount")

    table.add_row("", "")
    table.add_row("SCALING PARAMETERS", "", style="bold")
    addRow("Cooldown Period", key="cooldownPeriodSeconds", ending="s")
    addRow("Minimum Replicas")
    if "maxReplicaCount" in data:
        addRow("Maximum Replicas", key="maxReplicaCount", optional=True)

    table.add_row("", "")
    table.add_row("STATUS", "", style="bold")
    addRow("Status", "status", value=_status_color(get("status")))
    addRow("Last Build Status", value=_status_color(get("lastBuildStatus")))
    addRow("Last Build Version", value=get("latestBuildVersion"), optional=True)

    if data.get("pods"):
        table.add_row("", "")
        table.add_row(
            "[bold]LIVE PODS[/bold]", "\n".join(data.get("pods", "Data Unavailable"))
        )

    return table
