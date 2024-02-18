import json
import os
import re
import sys
import tempfile
import time
import zipfile
from typing import List, Union

import requests
from tenacity import retry, stop_after_delay, wait_fixed
from termcolor import colored
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper
from yaspin import yaspin
from yaspin.core import Yaspin
from yaspin.spinners import Spinners

import cerebrium.utils as utils
from cerebrium import verification
from cerebrium.errors import CerebriumRequestError
from cerebrium.utils import env

dashboard_url = (
    os.environ["DASHBOARD_URL"]
    if "DASHBOARD_URL" in os.environ
    else (
        "https://dev-dashboard.cerebrium.ai"
        if env == "dev"
        else "https://dashboard.cerebrium.ai"
    )
)

api_url = (
    os.environ["REST_API_URL"]
    if "REST_API_URL" in os.environ
    else (
        "https://dev-rest-api.cerebrium.ai"
        if env == "dev"
        else "https://rest-api.cerebrium.ai"
    )
)

stream_logs_url = (
    os.environ["STREAM_LOGS_URL"]
    if "STREAM_LOGS_URL" in os.environ
    else (
        "https://gklwrtbtdgb4fvs72bw5j2ap3q0omics.lambda-url.eu-west-1.on.aws"
        if env == "dev"
        else "https://icnl4trzmhm422rmqbyp4pgniq0uresm.lambda-url.eu-west-1.on.aws"
    )
)

error_messages = {
    "disk quota exceeded": "💾 You've run out of space in your /persistent-storage. \n"
    "You can add more by running the command: `cerebrium storage --increase-in-gb <the_amount_in_GB>`"
}  # Error messages to check for
__LOG_DEBUG_DELIMITERS__ = ["|| DEBUG ||", "|| END DEBUG ||"]
__LOG_INFO_DELIMITERS__ = ["|| INFO ||", "|| END INFO ||"]
__LOG_ERROR_DELIMITERS__ = ["|| ERROR ||", "|| END ERROR ||"]

__re_debug__ = re.compile(r"^\|\| DEBUG \|\| (.*) \|\| END DEBUG \|\|")
__re_info__ = re.compile(r"^\|\| INFO \|\| (.*) \|\| END INFO \|\|")
__re_error__ = re.compile(r"^\|\| ERROR \|\| (.*) \|\| END ERROR \|\|")


def colourise_log(log: str, add_prefix: bool = True) -> str:
    """
    Strip the log level delimiters and colourise the log message based on the log level.
    Leave the rest of the message unchanged.
    """
    prefixes = {"DEBUG": "DEBUG: |  ", "INFO": "INFO: |   ", "ERROR": "ERROR: |   "}
    re_replace = r"\1"
    while (
        __LOG_DEBUG_DELIMITERS__[0] in log
        or __LOG_INFO_DELIMITERS__[0] in log
        or __LOG_ERROR_DELIMITERS__[0] in log
    ):
        if __re_debug__.match(log):
            prefix = prefixes["DEBUG"] if add_prefix else ""
            log = __re_debug__.sub(colored(f"{prefix}{re_replace}", "yellow"), log)

        if __re_info__.match(log):
            prefix = prefixes["INFO"] if add_prefix else ""
            log = __re_info__.sub(re_replace, log)

        if __re_error__.match(log):
            prefix = prefixes["ERROR"] if add_prefix else ""
            log = __re_error__.sub(colored(f"{prefix}{re_replace}", "red"), log)

    return log


def _check_payload(method: str, payload: dict) -> None:
    """
    Check that the payload for a given method is valid.

    Args:
        payload (dict): The payload to check.

    Returns:
        bool: True if the payload is valid, False otherwise.
    """
    if method not in ("getUploadUrl", "checkDeploymentStatus"):
        utils.cerebrium_log(
            prefix="ValueError",
            message=f"Method '{method}' not supported",
            level="ERROR",
        )
    if "name" not in payload:
        utils.cerebrium_log(
            prefix="ValueError",
            message=f"Payload for '{method}' must contain 'name' key",
            level="Error",
        )


def _cerebrium_request(
    method: str,
    http_method: str,
    api_key: str,
    payload: Union[dict, None] = None,
    enable_spinner: bool = False,
    pending_text: str = "",
    end_text: str = "",
) -> dict:
    """
    Make a request to the Cerebrium API.

    Args:
        method (str): The server method to use.
        api_key (str): The API key for the Cerebrium account.
        payload (dict): The payload to send with the request.
        enable_spinner (bool): A toggle to enable the spinner.
        pending_text (str): The text to display while the request is pending.
        end_text(str): The text to display when the request is complete.

    Returns:
        dict ('status_code': int, 'data': dict): The response code and data.
    """

    headers = {"Authorization": api_key, "ContentType": "application/json"}
    url = f"{api_url}/{method}"

    # Make a request to the Cerebrium API
    @retry(stop=stop_after_delay(60), wait=wait_fixed(8))
    def _request():
        data = None if payload is None else json.dumps(payload)
        if http_method == "POST":
            response = requests.post(url, headers=headers, data=data, timeout=30)
        else:
            response = requests.get(url, headers=headers, params=payload, timeout=30)
        return {"status_code": response.status_code, "data": json.loads(response.text)}

    if enable_spinner:
        with yaspin(Spinners.arc, text=pending_text, color="magenta"):
            response = _request()
        if response["status_code"] == 200:
            print(f"✅ {end_text}")
        else:
            print(f"✗ {end_text}")
            raise CerebriumRequestError(
                response["status_code"],
                method,
                response["data"],
            )
    else:
        response = _request()
    return response


def _check_response(
    response: requests.Response,
    key: Union[str, None] = None,
    error_msg="API request failed:",
    empty_response_okay: bool = False,
    spinner: Union[yaspin, None] = None,
) -> bool:
    """
    Check the response from the Cerebrium API for errors.

    Args:
        response (requests.Response): API response.
        key (str): Key param that the response should contain.
        error_msg (str, optional) = "API request failed": The error message output.
        empty_response_okay (bool, optional) = False: Whether an empty response is okay.
        spinner (Yaspin, optional) = None: The spinner to update.

    Returns:
        bool: True if the response is valid, False otherwise.
    """
    message = (
        f"Status code: {response.status_code}\n" if response.status_code != 200 else ""
    )
    # Check if the text is valid json or an error message
    response_json = {}
    try:
        response_json = json.loads(response.text or '{"message": "No data returned"}')
    except json.decoder.JSONDecodeError:
        if not response.text:
            message += "Response text is empty, caused json parse error:"
        else:
            message += f"Response text is not valid json: {response.text}"
        utils.cerebrium_log(
            level="ERROR", message=message, prefix=error_msg, spinner=spinner
        )

    if key is not None and not empty_response_okay:
        fail = response.status_code != 200 or (response_json.get(key, None) is None)
    else:
        fail = response.status_code != 200

    if fail:
        if response_json.get("message", None):
            message += response_json.get("message", "")
        else:
            message += response.text
        utils.cerebrium_log(
            level="ERROR", message=message, prefix=error_msg, spinner=spinner
        )
        return False
    return True


def _setup_app(headers: dict, body: dict, url=f"{api_url}/setupApp") -> dict:
    """
    Set up the app on Cerebrium for a run or deployment.
    """
    upload_url_response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    _check_response(
        response=upload_url_response,
        key="status",
        error_msg="Error getting upload URL:",
    )
    return upload_url_response.json()


def _poll_app_status(
    api_key: str,
    build_id: str,
    app_id: str,
    disable_animation: bool,
    disable_build_logs: bool,
    is_code_change: bool = False,
    timeout_seconds=30 * 60,
    is_run: bool = False,
    gpu: str = "AMPERE_A6000",
    poll_logs: bool = True,
) -> str:
    """
    Poll the deployment status of a conduit.

    Args:
        api_key (str): The API key for the Cerebrium account.
    """
    # Check the status of the deployment by polling the Cerebrium API for deployment status
    # Poll the streamBuildLogs endpoint with yaspin for max of 10 minutes to get the build status
    print("----------------------------------------")

    # hardware_unavailable_messaged = False
    build_status = "IN_PROGRESS"

    spinner_status = "🧱 Setting Up Builder..."
    if is_code_change:
        spinner_status = "🔨 Syncing code change..."
        build_status = "success"

    spinner = None
    if not disable_animation:
        spinner = yaspin(text=spinner_status, color="yellow")
        spinner.start()
    else:
        print(spinner_status)

    if poll_logs:
        build_status = _poll_logs(
            api_key=api_key,
            build_id=build_id,
            seen_index=0,
            spinner=spinner,
            build_status=build_status,
            spinner_status=spinner_status,
            disable_build_logs=disable_build_logs,
            is_code_change=is_code_change,
            timeout_seconds=timeout_seconds,
            is_run=is_run,
            gpu=gpu,
        )
    else:
        build_status = _stream_logs(
            api_key=api_key,
            app_id=app_id,
            build_id=build_id,
            build_status=build_status,
            spinner_status=spinner_status,
            spinner=spinner,
            disable_build_logs=disable_build_logs,
            is_run=is_run,
            gpu=gpu,
        )

    if spinner:
        spinner.write(spinner_status)
        spinner.stop()
        spinner.text = ""

    if build_status in ("success", "build_success"):
        msg = "🚀 Build complete!\n"
        if spinner:
            spinner.ok(msg)
        else:
            print(msg)
    return build_status


def _stream_logs(
    api_key: str,
    app_id: str,
    build_id: str,
    build_status: str,
    spinner_status: str,
    spinner: Yaspin,
    disable_build_logs: bool,
    is_run: bool = False,
    gpu: str = "AMPERE_A6000",
    timeout_seconds=30 * 60,
) -> str:
    start_time = time.time()
    url = f"{stream_logs_url}/?modelId={app_id}&buildId={build_id}"
    headers = {
        "Authorization": api_key,
        "Content-Type": "text/event-stream",
        "Transfer-Encoding": "chunked",
        "Connection": "keep-alive",
    }

    def finish(spinner, build_status):
        if spinner:
            spinner.write(spinner_status)
            spinner.stop()
            spinner.text = ""

        if build_status in ("success", "build_success"):
            msg = "🚀 Build complete!\n"
            if spinner:
                spinner.ok(msg)
            else:
                print(msg)

        return build_status

    _log_text(msg="📜 Streaming build logs...", spinner=spinner)

    # print("DEBUG: curl: ")
    # print(f"curl -X POST {url}", end=" \\\n \t-H ")
    # print(" \\ \n\t -H ".join([f"'{k}: {v}'" for k, v in headers.items()]))

    while (
        (time.time() - start_time < timeout_seconds)
        and "failure" not in build_status
        and "success" not in build_status
    ):
        with requests.get(
            url, headers=headers, stream=True, timeout=timeout_seconds
        ) as response:
            build_status = _get_build_status(api_key=api_key, build_id=build_id)
            spinner_status = _log_status(
                build_status=build_status,
                spinner=spinner,
                spinner_status=spinner_status,
                start_time=start_time,
                gpu=gpu,
                is_run=is_run,
            )
            for line in response.iter_lines():
                # convert line bytes to utf-8 string
                line = line.decode("utf-8")
                if not line:
                    continue
                if not disable_build_logs:
                    _update_log_stream(
                        logs=line, spinner=spinner, spinner_status=spinner_status
                    )
                    if build_status == "success":
                        finish(spinner=spinner, build_status=build_status)

    if time.time() - start_time > timeout_seconds:
        msg = "⏲️ Polling build logs timed out."
        _log_fail(msg=msg, spinner=spinner, spinner_status=spinner_status)

    if "failure" not in build_status:
        _log_text(msg="📜 End of build log stream.", spinner=spinner)

    return build_status


def _get_build_status(api_key, build_id) -> str:
    """Get the build status of a build from the backend"""
    build_status_response = requests.get(
        f"{api_url}/getBuildStatus",
        params={"buildId": build_id},
        headers={"Authorization": api_key, "Content-Type": "application/json"},
    )
    # if the response is not 200, print error and exit
    _check_response(
        response=build_status_response,
        error_msg="Error getting build status:",
        key="status",
    )
    build_status = build_status_response.json()["status"]
    return build_status


def _poll_logs(
    api_key: str,
    build_id: str,
    seen_index: int,
    spinner: Yaspin,
    build_status: str,
    spinner_status: str,
    disable_build_logs: bool,
    is_code_change: bool = False,
    timeout_seconds=30 * 60,
    is_run: bool = False,
    gpu: str = "AMPERE_A6000",
):
    seen_index = 0
    start_time = time.time()
    while (build_status != "success") and (not is_code_change):
        logs_response = requests.get(
            f"{api_url}/streamBuildLogs",
            params={"buildId": build_id},
            headers={"Authorization": api_key, "Content-Type": "application/json"},
        )
        # if the response is not 200, print error and exit
        _check_response(response=logs_response, error_msg="Error getting build logs:")
        build_status = _get_build_status(api_key=api_key, build_id=build_id)
        response_logs = logs_response.json()["logs"]
        concat_logs = "".join(response_logs)
        logs = concat_logs.split("\n")[:-1]
        logs = logs[seen_index:]

        if not disable_build_logs:
            spinner_status = _log_status(
                build_status=build_status,
                spinner=spinner,
                spinner_status=spinner_status,
                start_time=start_time,
                gpu=gpu,
                is_run=is_run,
            )
            _update_log_stream(
                logs=logs, spinner=spinner, spinner_status=spinner_status
            )
        seen_index += len(logs)

        if time.time() - start_time > timeout_seconds:
            msg = "⏲️ Polling build logs timed out."
            _log_fail(msg=msg, spinner=spinner, spinner_status=spinner_status)
        elif "failure" in build_status:
            msg = f"🚨 Build failed with status: {build_status}"
            _log_fail(msg=msg, spinner=spinner, spinner_status=spinner_status)
        elif build_status == "success":
            break
    return build_status


def _log_fail(msg: str, spinner: Yaspin, spinner_status: str):
    if spinner:
        spinner.write(spinner_status)
        spinner.text = ""
        spinner.fail(msg)
        spinner.stop()
        sys.exit(1)
    else:
        utils.cerebrium_log(level="ERROR", message=msg, prefix="Build Failed with:")


def _log_status(
    build_status,
    spinner: Yaspin,
    spinner_status: str,
    start_time: float,
    gpu: str,
    is_run: bool = False,
) -> str:
    msg = "polling logs..."
    if build_status == "building":
        msg = "🔨 Building App..."
    elif build_status == "initializing":
        if is_run:
            msg = "🛠️ Initializing Run..."
        else:
            msg = "🛠️ Initializing Build..."
    elif build_status == "synchronizing_files":
        msg = "📂 Syncing files..."
    elif build_status == "pending":
        msg = "⏳ Build pending..."
        # if build is stuck initialising, suggest new hardware.
        if time.time() - start_time > 90:
            new_hardware = {
                "AMPERE_A100": "AMPERE_A6000",
                "AMPERE_A6000": "AMPERE_A5000",
                "AMPERE_A5000": "TURING_5000",
                "AMPERE_A4000": "TURING_4000",
            }.get(gpu, "a different GPU")

            msg = colored(
                text=(
                    f"⏳ Build pending... Hardware unavailable at the moment. Try use {new_hardware}."
                ),
                color="yellow",
            )

        elif time.time() - start_time > 30:
            msg = "⏳ Build pending... this is taking longer than usual"
        elif time.time() - start_time > 25:
            msg = (
                "⏳ Build pending... we're still trying to provision your hardware."
                " Hang tight."
            )
        elif time.time() - start_time > 15:
            msg = (
                "⏳ Build pending ... provisioning your hardware."
                " This usually takes a few seconds."
            )
    elif build_status == "failed":
        msg = "🚨 Build failed!"
    else:
        msg = build_status

    if spinner and msg != spinner_status:
        spinner.text = msg
    elif msg != spinner_status:
        print(msg)
    return msg


def _log_text(msg: str, spinner: Union[Yaspin, None]):
    if msg == "":
        return
    if spinner:
        spinner.write(msg)
    else:
        print(msg)


def _update_log_stream(
    logs: List[str],
    spinner: Union[Yaspin, None] = None,
    spinner_status: str = "",
):
    if isinstance(logs, str):
        logs = [logs]
    for log in logs:
        message = str(log)
        if message:
            match = re.match(
                r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9})Z ", message
            )
            if match is not None:  # If the regex matches the beginning of the string
                created = match[1]
                message = message[len(created) + 2 :]
                for e in error_messages:
                    if e in message.lower():
                        msg = (
                            f"{message[:message.find(e)]}\n"
                            "\n🚨 Build failed! \n"
                            f"{error_messages[e]}"
                        )
                        _log_fail(
                            msg=msg, spinner=spinner, spinner_status=spinner_status
                        )
            message = colourise_log(message)
            # append a newline to the message if it doesn't already have one.
            # Else, yaspin will not break lines in progress bars and end up filling the terminal
            message = message.strip("\n").strip("\r").strip("\r\n")
            if message:
                _log_text(msg=f"{message}\n", spinner=spinner)
        _log_text(msg="", spinner=spinner)


def upload_cortex_files(
    upload_url: str,
    zip_file_name: str,
    file_list: list,
    disable_syntax_check: bool = False,
    disable_animation: bool = False,
    predict_data: Union[None, str] = None,
    requirements={},
    pkglist=[],
    conda_pkglist=[],
) -> bool:
    if file_list == []:
        utils.cerebrium_log(
            level="ERROR",
            message="No files to upload.",
            prefix="Error uploading app to Cerebrium:",
        )

    # Remove requirements.txt, pkglist.txt, conda_pkglist.txt from file_list if they exist. Will be added from config
    if "requirements.txt" in file_list:
        file_list.remove("requirements.txt")
    if "conda_pkglist.txt" in file_list:
        file_list.remove("conda_pkglist.txt")
    if "pkglist.txt" in file_list:
        file_list.remove("pkglist.txt")
    if "./requirements.txt" in file_list:
        file_list.remove("./requirements.txt")
    if "./conda_pkglist.txt" in file_list:
        file_list.remove("./conda_pkglist.txt")
    if "./pkglist.txt" in file_list:
        file_list.remove("./pkglist.txt")

    # Zip all files in the current directory and upload to S3
    with tempfile.TemporaryDirectory() as temp_dir:
        zip_path = os.path.join(temp_dir, zip_file_name)
        dir_name = os.path.dirname(zip_path)

        # write a predict config file containing the prediction parameters
        predict_file = os.path.join(
            temp_dir, "_cerebrium_predict.json"
        )  # use a file to avoid storing large files in the model objects in ddb
        if predict_data:
            with open(predict_file, "w") as f:
                f.write(
                    predict_data
                )  # predict data has been validated as a json string previously

        os.makedirs(dir_name, exist_ok=True)
        with zipfile.ZipFile(zip_path, "w") as zip_file:
            if not disable_syntax_check:
                verification.run_pyflakes(files=file_list, print_warnings=True)

            print("🗂️  Zipping files...")
            for f in file_list:
                if os.path.isfile(f):
                    zip_file.write(f)

            if predict_data:
                zip_file.write(predict_file, arcname=os.path.basename(predict_file))

            if requirements:
                utils.requirements_to_file(
                    requirements, os.path.join(temp_dir, "requirements.txt")
                )
                zip_file.write(
                    os.path.join(temp_dir, "requirements.txt"),
                    arcname="requirements.txt",
                )
            if pkglist:
                utils.requirements_to_file(
                    pkglist, os.path.join(temp_dir, "pkglist.txt")
                )
                zip_file.write(
                    os.path.join(temp_dir, "pkglist.txt"), arcname="pkglist.txt"
                )
            if conda_pkglist:
                utils.requirements_to_file(
                    conda_pkglist, os.path.join(temp_dir, "conda_pkglist.txt")
                )
                zip_file.write(
                    os.path.join(temp_dir, "conda_pkglist.txt"),
                    arcname="conda_pkglist.txt",
                )

        print("⬆️  Uploading to Cerebrium...")
        with open(zip_path, "rb") as f:
            headers = {
                "Content-Type": "application/zip",
            }
            if not disable_animation:
                with tqdm(
                    total=os.path.getsize(zip_path),
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    colour="#EB3A6F",
                ) as pbar:  # type: ignore
                    wrapped_f = CallbackIOWrapper(pbar.update, f, "read")
                    upload_response = requests.put(
                        upload_url,
                        headers=headers,
                        data=wrapped_f,  # type: ignore
                        timeout=60,
                        stream=True,
                    )
            else:
                upload_response = requests.put(
                    upload_url,
                    headers=headers,
                    data=f,
                    timeout=60,
                    stream=True,
                )

            _check_response(
                response=upload_response,
                key=None,
                error_msg="Error uploading app to Cerebrium:",
            )
            print("✅ Resources uploaded successfully.")
            return True
