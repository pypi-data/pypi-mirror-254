import json
import sys
import requests
import typer
from typing_extensions import Annotated, Optional

import cerebrium.utils as utils
from cerebrium.api import api_url, _check_response
from cerebrium.core import cli


@cli.command()
def storage(
    increase_in_gb: Annotated[
        int,
        typer.Option(
            help="Increase storage capacity by the given number of GB. Warning: storage cannot be decreased once allocated and this will increase your monthly bill.",
            min=0,
        ),
    ] = 0,
    get_capacity: Annotated[
        bool,
        typer.Option(
            help="Get the current storage capacity you have allocated to this project.",
        ),
    ] = False,
    api_key: Annotated[
        Optional[str],
        typer.Option(
            help="Private API key for your project. If not provided, will use the API key from your cerebrium login.",
        ),
    ] = None,
):
    """A lightweight utility to view persistent storage capacity and increase it."""
    if not api_key:
        api_key = utils.get_api_key()
    if not api_key:
        utils.cerebrium_log(message="Please provide an API key.", level="ERROR")

    if get_capacity:
        response = requests.get(
            f"{api_url}/get-storage-capacity",
            headers={"Authorization": api_key},
        )

        _check_response(response, key="capacity")
        print(f"📦 Storage capacity: {json.loads(response.text).get('capacity')} GB")
        sys.exit(0)

    if increase_in_gb:
        print(f"📦 Increasing storage capacity by {increase_in_gb}GB...")
        response = requests.post(
            f"{api_url}/increase-storage-capacity",
            headers={"Authorization": api_key},
            json={"increaseInGB": increase_in_gb},
        )

        _check_response(response, key="capacity")
        new_size = json.loads(response.text).get("capacity")
        print(f"✅ Storage capacity successfully increased to {new_size} GB.")
        sys.exit(0)
