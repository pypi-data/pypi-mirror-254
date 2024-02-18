import json
import os
import re
import tempfile

from cerebrium import datatypes
import cerebrium.utils as utils
from cerebrium import __version__ as cerebrium_version


def run_pyflakes(
    dir="",
    files=[],
    print_warnings=True,
):
    import pyflakes.api
    from pyflakes.reporter import Reporter

    with tempfile.TemporaryDirectory() as tmp:
        warnings_log_file = os.path.join(tmp, "warnings.log")
        errors_log_file = os.path.join(tmp, "errors.log")

        with open(errors_log_file, "w") as warnings_log, open(
            warnings_log_file, "w"
        ) as errors_log:
            reporter = Reporter(warningStream=warnings_log, errorStream=errors_log)
            if dir:
                pyflakes.api.checkRecursive([dir], reporter=reporter)
            elif files:
                for filename in files:
                    if os.path.splitext(filename)[1] != ".py":
                        continue
                    code = open(filename, "r").read()
                    pyflakes.api.check(code, filename, reporter=reporter)

        with open(warnings_log_file, "r") as f:
            warnings = f.readlines()

        with open(errors_log_file, "r") as f:
            errors = f.readlines()

    filtered_errors = []
    for e in errors:
        if e.count("imported but unused") > 0:
            warnings.append(e)
        else:
            filtered_errors.append(e)

    if warnings and print_warnings:
        warnings_to_print = "".join(warnings)
        utils.cerebrium_log(
            prefix="Warning: Found the following warnings in your files.",
            message=f"\n{warnings_to_print}",
            level="WARNING",
        )

    if filtered_errors:
        errors_to_print = "".join(filtered_errors)
        utils.cerebrium_log(
            prefix="Error: Found the following syntax errors in your files:",
            message=f"{errors_to_print}"
            "Please fix the errors and try again. \nIf you would like to ignore these errors and deploy anyway, use the `--disable-syntax-check` flag.",
            level="ERROR",
        )
    return errors, warnings


def validate_name(name: str) -> str:
    """Validate the name of the deployment"""
    message = ""
    if not name:
        message += "No name provided.\n"
        return message

    # max len = 63 less len({stage}-{projectId(10chars)}-{name}-{stage}-build-{id(8chars)})
    max_l = 32 if utils.env == "prod" else 63 - 28 - 2 * len(utils.env)
    if len(name) > max_l:
        message += f"Name must be at most {max_l} characters.\n"

    # only allow lower case letters, numbers, and dashes
    if not re.match("^[a-z0-9\\-]*$", name):
        message += "Name must only contain lower case letters, numbers, and dashes.\n"
    return message


def validate_python_version(python_version: str) -> str:
    message = ""
    if not python_version:
        return message

    vals = [v.value for v in datatypes.PythonVersion]
    if python_version not in vals:
        message += f"Python version must be one of {vals}\n"

    return message


def validate_gpu_selection(user_hardware: str) -> str:
    message = ""
    # Check that hardware is valid and assign to enum
    if not user_hardware:
        print(f"No GPU provided. Defaulting to {datatypes.DEFAULT_GPU_SELECTION}.")
        return ""

    if user_hardware not in datatypes.Hardware.available_hardware():
        message += (
            f"Hardware must be one of:{datatypes.Hardware.available_hardware()}\n"
        )
    return message


def validate_cooldown(cooldown) -> str:
    message = ""
    if not cooldown:
        return message
    if cooldown < 0:
        message += "Cooldown must be a non-negative number of seconds.\n"
    return message


def validate_min_replicas(min_replicas) -> str:
    """Validate the minimum number of replicas"""
    message = ""
    if min_replicas is None or min_replicas == "":
        return message
    if min_replicas < 0 or not isinstance(min_replicas, int):
        message += "Minimum number of replicas must be a non-negative integer.\n"
    return message


def validate_max_replicas(max_replicas, min_replicas) -> str:
    """Validate the maximum number of replicas"""
    message = ""
    if max_replicas is None or max_replicas == "":
        return message
    if max_replicas < 1 or not isinstance(max_replicas, int):
        message += "Maximum number of replicas must be a non-negative integer greater than 0.\n"
    if max_replicas < min_replicas:
        message += "Maximum number of replicas must be greater than or equal to minimum number of replicas.\n"
    return message


def validate_and_update_cortex_params(
    config: datatypes.CerebriumConfig,
) -> datatypes.CerebriumConfig:
    """Validate the cortex deployment"""

    message = ""
    message += validate_name(config.deployment.name)
    gpu_message = validate_gpu_selection(config.hardware.gpu)
    message += gpu_message
    message += validate_python_version(config.deployment.python_version)
    message += validate_cooldown(config.scaling.cooldown)
    message += validate_min_replicas(config.scaling.min_replicas)
    if config.scaling.max_replicas is not None:
        message += validate_max_replicas(
            config.scaling.max_replicas, config.scaling.min_replicas
        )

    if gpu_message:
        utils.cerebrium_log(message=message, level="ERROR")

    gpu_option = getattr(datatypes.Hardware, config.hardware.gpu)
    if config.hardware.gpu_count is None:
        config.hardware.gpu_count = 1 if config.hardware.gpu != "CPU" else 0
    if config.hardware.memory is None:
        config.hardware.memory = (
            datatypes.DEFAULT_MEMORY
            if config.hardware.gpu.upper() != "CPU"
            else config.hardware.cpu * gpu_option.max_memory_per_cpu
        )

        message += gpu_option.validate(
            cpu=config.hardware.cpu,
            memory=config.hardware.memory,
            gpu_count=config.hardware.gpu_count,
        )

    if message:
        utils.cerebrium_log(message=message, level="ERROR")

    return config


def get_config(
    config_file,
    name,
    cpu,
    exclude,
    gpu,
    include,
    force_rebuild,
    gpu_count,
    hide_public_endpoint,
    python_version,
    memory,
    disable_animation,
    disable_build_logs,
    disable_syntax_check,
    disable_confirm=False,
    cooldown=datatypes.DEFAULT_COOLDOWN,
    disable_predict=None,
    init_debug=False,
    log_level="INFO",
    min_replicas=None,
    max_replicas=None,
    predict_data=None,
    cuda_version="12",
) -> datatypes.CerebriumConfig:
    """Get the config file and override the default params with the config file params"""
    # Set default params

    # If a config file is provided, load it in.
    if config_file == "" or config_file is None:
        config_file = "cerebrium.toml"
    else:
        if not os.path.exists(config_file):
            utils.cerebrium_log(
                level="ERROR",
                message=f"Config file {config_file} not found.",
                prefix="Argument Error:",
            )
    config = utils.load_config(
        name=name, config_file=config_file, disable_confirmation=disable_confirm
    )
    disable_animation = disable_animation if disable_animation is not None else False
    # Override the default params with the config file params

    new_hardware = {"cpu": cpu, "gpu": gpu, "memory": memory, "gpu_count": gpu_count}
    new_hardware = utils.remove_null_values(new_hardware)

    new_deployment = {
        "name": name,
        "python_version": python_version,
        "include": include,
        "exclude": exclude,
    }
    new_deployment = utils.remove_null_values(new_deployment)

    new_scaling = {
        "cooldown": cooldown,
        "min_replicas": min_replicas,
        "max_replicas": max_replicas,
    }
    new_scaling = utils.remove_null_values(new_scaling)

    new_build = {
        "force_rebuild": force_rebuild,
        "hide_public_endpoint": hide_public_endpoint,
        "disable_animation": disable_animation,
        "disable_build_logs": disable_build_logs,
        "disable_syntax_check": disable_syntax_check,
        "disable_predict": disable_predict,
        "disable_confirmation": disable_confirm,
        "predict_data": predict_data,
        "init_debug": init_debug,
        "log_level": log_level,
    }
    new_build = utils.remove_null_values(new_build)

    config.hardware.__dict__.update(new_hardware)
    config.deployment.__dict__.update(new_deployment)
    config.scaling.__dict__.update(new_scaling)
    config.build.__dict__.update(new_build)

    CerebriumConfig = validate_and_update_cortex_params(config)

    # This should now be the source of ground truth for the config
    return CerebriumConfig


def validate_cortex(
    name,
    config_file="",
    cpu=datatypes.DEFAULT_CPU,
    gpu=datatypes.DEFAULT_GPU_SELECTION,
    gpu_count=datatypes.DEFAULT_GPU_COUNT,
    python_version=datatypes.DEFAULT_PYTHON_VERSION,
    memory=datatypes.DEFAULT_MEMORY,
    cooldown=datatypes.DEFAULT_COOLDOWN,
    min_replicas=datatypes.DEFAULT_MIN_REPLICAS,
    max_replicas=None,
    include=datatypes.DEFAULT_INCLUDE,
    exclude=datatypes.DEFAULT_EXCLUDE,
    force_rebuild=False,
    hide_public_endpoint=False,
    disable_animation=False,
    disable_build_logs=False,
    disable_syntax_check=False,
    disable_predict=False,
    init_debug=False,
    log_level="INFO",
    predict_data=None,
    disable_confirmation=False,
    cerebrium_function="deploy",
    cuda_version="12",
) -> dict:
    gpu = gpu.upper() if isinstance(gpu, str) else gpu
    log_level = log_level.upper() if isinstance(log_level, str) else log_level

    config = get_config(
        config_file=config_file,
        name=name,
        cpu=cpu,
        exclude=exclude,
        gpu=gpu,
        include=include,
        force_rebuild=force_rebuild,
        gpu_count=gpu_count,
        hide_public_endpoint=hide_public_endpoint,
        python_version=python_version,
        memory=memory,
        disable_animation=disable_animation,
        disable_build_logs=disable_build_logs,
        disable_syntax_check=disable_syntax_check,
        cooldown=cooldown,
        disable_predict=disable_predict,
        disable_confirm=disable_confirmation,
        init_debug=init_debug,
        log_level=log_level,
        min_replicas=min_replicas,
        max_replicas=max_replicas,
        predict_data=predict_data,
        cuda_version=cuda_version,
    )
    config.cerebrium_version = cerebrium_version

    if not os.path.exists("./main.py"):
        utils.cerebrium_log(
            level="ERROR",
            message="main.py not found in current directory. " "This file is required.",
            prefix="Deployment Requirements Error:",
        )

    if cuda_version not in ["11", "12"]:
            utils.cerebrium_log(
                level="ERROR",
                message="CUDA version must be one of 11 or 12.",
                prefix="Deployment CUDA Error:",
            )

    with open("./main.py", "r") as f:
        main_py = f.read()
        if "def predict(" not in main_py:
            utils.cerebrium_log(
                level="ERROR",
                message="main.py does not contain a predict function."
                " This function is required.",
                prefix="Deployment Requirements Error:",
            )

    if config.build.disable_predict:
        config.build.predict_data = None
    else:
        if config.build.predict_data is None:
            utils.cerebrium_log(
                level="ERROR",
                message="No predict data provided. "
                "Please provide predict_data in json format to your cerebrium.toml.\n"
                "This data is used to test your predict function on build to ensure "
                "your new deployment will work as you expect before replacing your "
                "existing deployment.\n"
                "Otherwise, use the `--disable-predict` flag to disable the check",
                prefix="Argument Error:",
            )
        else:
            try:
                json.dumps(json.loads(config.build.predict_data), indent=4)
            except json.decoder.JSONDecodeError:
                utils.cerebrium_log(
                    message="Invalid JSON string",
                    level="ERROR",
                    prefix="Could not parse predict data:",
                )
    if config.build.disable_confirmation:
        utils.cerebrium_log(
            message="Disabling confirmation. This will automatically deploy your model.",
            level="WARNING",
        )

    if not utils.confirm_deployment(
        config=config,
        cerebrium_function=cerebrium_function,
        disable_confirmation=config.build.disable_confirmation,
    ):
        utils.cerebrium_log(
            level="ERROR",
            message="Adjust the parameters in your cerebrium.toml and redeploy!",
            prefix="Deployment Cancelled:",
        )

    return config
