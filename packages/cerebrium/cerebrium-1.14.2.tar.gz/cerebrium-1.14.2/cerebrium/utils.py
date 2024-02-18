import copy
import fnmatch
import hashlib
import os
import sys
import re
import yaml
import toml
import typer
from typing import Dict, List, Union
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich import print as console
from termcolor import colored
from yaspin import yaspin

# from cerebrium import datatypes
from . import datatypes

env = os.getenv("ENV", "prod")
RequirementsType = Union[Dict[str, str], List[str]]


def determine_includes(include, exclude):
    include_set = include.strip("[]").split(",")
    include_set.extend(
        [
            "./main.py",
            "./requirements.txt",
            "./pkglist.txt",
            "./conda_pkglist.txt",
        ]
    )
    include_set = set(map(ensure_pattern_format, include_set))
    include_set = [i.strip() for i in include_set]

    exclude_set = exclude.strip("[]").split(",")
    exclude_set = [e.strip() for e in exclude_set]
    exclude_set = set(map(ensure_pattern_format, exclude_set))

    file_list = []
    for root, _, files in os.walk("./"):
        for file in files:
            full_path = os.path.join(root, file)
            if any(
                fnmatch.fnmatch(full_path, pattern) for pattern in include_set
            ) and not any(
                fnmatch.fnmatch(full_path, pattern) for pattern in exclude_set
            ):
                print(f"➕ Adding {full_path}")
                file_list.append(full_path)
    return file_list


def get_api_key():
    config_path = os.path.expanduser("~/.cerebrium/config.yaml")
    msg = (
        "Please login using 'cerebrium login <private_api_key>' "
        "or specify the key using the `--api-key` flag."
    )
    if not os.path.exists(config_path):
        cerebrium_log(level="ERROR", message=msg)

    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    if env == "dev":
        print("❗️❗️Logging in with dev API key❗️❗️")
        key_name = "dev_api_key"
    else:
        key_name = "api_key"

    if config is None or key_name not in config:
        cerebrium_log(level="ERROR", message=msg)

    return config[key_name]


def ensure_pattern_format(pattern):
    if not pattern.startswith("./"):
        pattern = f"./{pattern}"
    elif pattern.startswith("/"):
        cerebrium_log(
            prefix="ValueError",
            level="Error",
            message="Pattern cannot start with a forward slash. Please use a relative path.",
        )
    if pattern.endswith("/"):
        pattern = f"{pattern}*"
    elif os.path.isdir(pattern) and not pattern.endswith("/"):
        pattern = f"{pattern}/*"
    return pattern


def cerebrium_log(
    message: str,
    prefix: str = "",
    level: str = "INFO",
    attrs: list = [],
    color: str = "",
    end="\n",
    spinner: Union[yaspin(), None] = None,
):
    """User friendly coloured logging

    Args:
        message (str): Error message to be displayed
        prefix (str): Prefix to be displayed. Defaults to empty.
        level (str): Log level. Defaults to "INFO".
        attrs (list, optional): Attributes for colored printing. Defaults to None.
        color (str, optional): Color to print in. Defaults depending on log level.
        end (str, optional): End character. Defaults to "\n".
    """

    level = level.upper()
    default_prefixes = {"INFO": "Info: ", "WARNING": "Warning: ", "ERROR": "Error: "}
    default_colors = {"INFO": None, "WARNING": "yellow", "ERROR": "red"}
    prefix = prefix or default_prefixes.get(level, "")

    # None is default for unused variables to avoid breaking termcolor
    color = color or default_colors.get(level, "")
    prefix = colored(f"{prefix}", color=color, attrs=["bold"])
    message = colored(f"{message}", color=color, attrs=attrs)

    # spinners don't print nicely and keep spinning on errors. Use them if they're there
    if spinner:
        spinner.write(prefix)
        spinner.text = ""
        if level == "ERROR":
            spinner.fail(message)
            spinner.stop()
        else:
            spinner.write(message)
    else:
        print(prefix, end=end)
        print(message)

    if level == "ERROR":
        sys.exit(1)


def update_with_defaults(params: dict, defaults: dict):
    for key, val in defaults.items():
        if params.get(key) is None or params.get(key) == "":
            params[key] = val

    return params


def assign_param(param_dict: dict, key, new_value, default_value=None):
    param_dict[key] = (
        new_value if is_valid(new_value) else param_dict.get(key, default_value)
    )
    return param_dict


def is_valid(v):
    return (
        (isinstance(v, bool) and v is False) or bool(v) or isinstance(v, (int, float))
    )


def remove_null_values(param_dict: dict):
    new_dict = {}
    for key, val in param_dict.items():
        if isinstance(val, dict):
            val = remove_null_values(val)
        if val is not None:
            if not (isinstance(val, str) and val == ""):
                new_dict[key] = val
    return new_dict


def content_hash(files, strings=None) -> str:
    """
    Hash the content of each file, avoiding metadata.
    """

    files = files if isinstance(files, list) else [files]
    h = hashlib.sha256()
    if files:
        for file in files:
            if os.path.exists(file):
                with open(file, "rb") as f:
                    h.update(f.read())
            else:
                return "FILE_DOESNT_EXIST"

    if not isinstance(strings, list):
        strings = [strings]
    for string in strings:
        if isinstance(string, str):
            h.update(string.encode())
    if files or strings:
        return h.hexdigest()
    return "NO_FILES"


def check_deployment_size(files, max_size_mb=100):
    """
    Check if the sum of all files is less than max_size MB
    """
    files = files if isinstance(files, list) else [files]
    total_size = 0
    for file in files:
        if os.path.exists(file):
            total_size += os.path.getsize(file)

    return total_size > max_size_mb * 1024 * 1024


def confirm_deployment(
    config: datatypes.CerebriumConfig,
    cerebrium_function: str,
    disable_confirmation: bool = False,
):
    """
    Print out a confirmation message for the deployment
    - Display selected hardware options and configuration on a panel
    - Ask user to confirm
    """
    hardware = config.hardware
    deployment = config.deployment
    scaling = config.scaling
    build = config.build
    dependencies = config.dependencies

    def addOptionalRow(key, value):
        if value:
            deployment_table.add_row(key, str(value))

    deployment_table = Table(box=box.SIMPLE_HEAD)
    deployment_table.add_column("Parameter", style="")
    deployment_table.add_column("Value", style="")

    deployment_table.add_row("HARDWARE PARAMETERS", "", style="bold")
    deployment_table.add_row("GPU", str(hardware.gpu))
    deployment_table.add_row("CPU", str(hardware.cpu))
    deployment_table.add_row("Memory", str(hardware.memory))
    if hardware.gpu != "CPU":
        deployment_table.add_row("GPU Count", str(hardware.gpu_count))

    deployment_table.add_row("", "")
    if cerebrium_function == "run":
        deployment_table.add_row("RUN PARAMETERS", "", style="bold")
    else:
        deployment_table.add_row("DEPLOYMENT PARAMETERS", "", style="bold")
    deployment_table.add_row("Python Version", str(deployment.python_version))
    deployment_table.add_row("Include pattern", str(deployment.include))
    deployment_table.add_row("Exclude pattern", str(deployment.exclude))
    deployment_table.add_row("CUDA Version", str(deployment.cuda_version))

    deployment_table.add_row("", "")
    deployment_table.add_row("SCALING PARAMETERS", "", style="bold")
    deployment_table.add_row("Cooldown", str(scaling.cooldown))
    deployment_table.add_row("Minimum Replicas", str(scaling.min_replicas))
    if scaling.max_replicas is not None:
        deployment_table.add_row("Maximum Replicas", str(scaling.max_replicas))

    deployment_table.add_row("", "")
    deployment_table.add_row("BUILD PARAMETERS", "", style="bold")
    if build.log_level is not None:
        deployment_table.add_row("Log Level", str(build.log_level))
    if build.predict_data is not None:
        predict_data = str(build.predict_data)
        if len(predict_data) > 180:
            predict_data = predict_data[:180] + "..."
        deployment_table.add_row("Predict Data", predict_data)

    for key, value in build.__dict__.items():
        if key not in ["predict_data", "log_level"]:
            addOptionalRow(key, value)

    deployment_table.add_row("", "")
    deployment_table.add_row("DEPENDENCIES", "", style="bold")

    deployment_table.add_row(
        "pip", "".join(req_dict_to_str_list(dependencies.pip, for_display=True))
    )
    deployment_table.add_row(
        "apt", "".join(req_dict_to_str_list(dependencies.apt, for_display=True))
    )
    deployment_table.add_row(
        "conda", "".join(req_dict_to_str_list(dependencies.conda, for_display=True))
    )

    name = deployment.name
    config_options_panel = Panel.fit(
        deployment_table,
        title=f"[bold]🧠 Deployment parameters for {name} 🧠",
        border_style="yellow bold",
        width=100,
        padding=(1, 2),
    )
    print()
    console(config_options_panel)
    print()
    if not disable_confirmation:
        return typer.confirm(
            "Do you want to continue with the deployment?",
            default=True,
            show_default=True,
        )
    else:
        return True


def legacy_to_toml_structure(
    name: str,
    legacy_config,
    config_file: str,
    save_to_file: bool = True,
    pip: dict = {},
    apt: list = [],
    conda: dict = {},
    disable_confirmation: bool = False,
    overwrite: bool = False,
) -> datatypes.CerebriumConfig:
    # Tomls have the following format so they're less intimidating:
    # [cerebrium.hardware]
    # {all the hardware params like cpu, memory, etc}
    # [cerebrium.scaling]
    # {all the scaling params. Min/max replicas, cooldown, etc}
    # [cerebrium.deployment]
    # {all the deployment params. Python version, include, exclude, etc}
    # [cerebrium.requirements] (optional pip requirements)
    # {all the pip requirements}
    # [cerebrium.conda_requirements] (optional conda requirements)
    # {all the conda requirements}
    # [cerebrium.pkglist] (optional pkglist)

    """Upgrade legacy config file to use a more intuitive toml format"""
    legacy = ".yaml" in config_file or ".yml" in config_file

    upgrade_to_toml = False
    if legacy and not disable_confirmation:
        upgrade_prompt = colored(
            "Upgrade legacy config to toml?",
            "yellow",
        )
        if typer.confirm(upgrade_prompt):
            upgrade_to_toml = True
    dir_path = os.path.dirname(os.path.realpath(config_file))
    legacy_config = legacy_config or {}
    new_config = {}

    # Hardware
    hardware = datatypes.CerebriumHardware(
        gpu=legacy_config.get(
            "hardware" if legacy else "gpu", datatypes.DEFAULT_GPU_SELECTION
        ),
        cpu=legacy_config.get("cpu", datatypes.DEFAULT_CPU),
        memory=legacy_config.get("memory", datatypes.DEFAULT_MEMORY),
        gpu_count=legacy_config.get("gpu_count", datatypes.DEFAULT_GPU_COUNT),
    )

    deployment = datatypes.CerebriumDeployment(
        name=legacy_config.get("name"),
        python_version=legacy_config.get(
            "python_version", datatypes.DEFAULT_PYTHON_VERSION
        ),
        include=legacy_config.get("include", datatypes.DEFAULT_INCLUDE),
        exclude=legacy_config.get("exclude", datatypes.DEFAULT_EXCLUDE),
    )

    default_predict_data = '{"prompt": "Here is some example predict data for your config.yaml which will be used to test your predict function on build."}'
    build = datatypes.CerebriumBuild(
        predict_data=legacy_config.get("predict_data", default_predict_data),
        disable_predict=legacy_config.get("disable_predict")
        or legacy_config.get("disable_predict_data"),
        disable_build_logs=legacy_config.get("disable_build_logs"),
        disable_animation=legacy_config.get("disable_animation"),
        force_rebuild=legacy_config.get("force_rebuild"),
        disable_confirmation=legacy_config.get("disable_confirmation"),
        hide_public_endpoint=legacy_config.get("hide_public_endpoint"),
        disable_syntax_check=legacy_config.get("disable_syntax_check"),
    )

    # Scaling
    scaling = datatypes.CerebriumScaling(
        min_replicas=legacy_config.get("min_replicas", datatypes.DEFAULT_MIN_REPLICAS),
        max_replicas=legacy_config.get("max_replicas", datatypes.DEFAULT_MAX_REPLICAS),
        cooldown=legacy_config.get("cooldown", datatypes.DEFAULT_COOLDOWN),
    )

    # Requirements
    dependencies = {"pip": pip, "conda": conda, "apt": apt}
    if (
        os.path.exists(os.path.join(dir_path, "requirements.txt"))
        and os.stat(os.path.join(dir_path, "requirements.txt")).st_size != 0
        and legacy
    ):
        dependencies = update_from_file(
            "requirements.txt",
            dependencies,
            "pip",
            confirm=(not legacy) and (not disable_confirmation),
        )
        dependencies["pip"].update(req_list_to_dict(pip))
    else:
        dependencies["pip"] = req_list_to_dict(pip)
    if (
        os.path.exists(os.path.join(dir_path, "pkglist.txt"))
        and os.stat(os.path.join(dir_path, "pkglist.txt")).st_size != 0
        and legacy
    ):
        dependencies = update_from_file(
            "pkglist.txt",
            dependencies,
            "apt",
            confirm=(not legacy) and (not disable_confirmation),
        )
        dependencies["apt"].update(req_list_to_dict(apt))

    else:
        dependencies["apt"] = req_list_to_dict(
            apt
        )  # no versions for apt. So we just add the list

    if (
        os.path.exists(os.path.join(dir_path, "conda_pkglist.txt"))
        and os.stat(os.path.join(dir_path, "conda_pkglist.txt")).st_size != 0
        and legacy
    ):
        dependencies = update_from_file(
            "conda_pkglist.txt",
            dependencies,
            "conda",
            confirm=(not legacy) and (not disable_confirmation),
        )
        dependencies["conda"].update(req_list_to_dict(conda))
    else:
        dependencies["conda"] = req_list_to_dict(conda)

    new_config = datatypes.CerebriumConfig(
        hardware=hardware,
        deployment=deployment,
        scaling=scaling,
        build=build,
        dependencies=datatypes.CerebriumDependencies(**dependencies),
    )

    if name:
        new_config.deployment.name = name
    elif not new_config.deployment.name:
        new_config.deployment.name = os.path.basename(dir_path)

    if save_to_file or upgrade_to_toml:
        new_config_file = os.path.join(dir_path, "cerebrium.toml")
        save_config_to_toml_file(new_config, new_config_file, overwrite=overwrite)
        # move old config file to config.yaml.legacy
        if legacy:
            cwd = os.getcwd()
            if os.path.exists(config_file):
                os.rename(config_file, config_file + ".legacy")
            elif os.path.exists(os.path.join(cwd, "config.yaml")):
                os.rename(
                    os.path.join(cwd, "config.yaml"),
                    os.path.join(cwd, "config.yaml.legacy"),
                )

    return new_config


def save_config_to_toml_file(
    config: datatypes.CerebriumConfig, file: str, overwrite: bool = False
):
    # Write to file
    config_dict = copy.deepcopy(config)
    config_dict = config_dict.to_dict()
    if "local_files" in config_dict:
        config_dict.pop("local_files")
    if "cerebrium_version" in config_dict:
        config_dict.pop("cerebrium_version")
    if "api_key" in config_dict:
        config_dict.pop("api_key")
    if "partial_upload" in config_dict:
        config_dict.pop("partial_upload")

    if "init_debug" in config_dict.get("build", {}):
        config_dict["build"].pop("init_debug")

    for k, v in config_dict.items():
        if hasattr(v, "to_dict"):
            config_dict[k] = v.to_dict()

    # sort the keys
    keys = list(config_dict.keys())
    keys.sort()
    config_dict = {k: config_dict[k] for k in keys}
    # make sure "requirements" is last key
    config_dict["dependencies"] = config_dict.pop("dependencies")
    config_dict = {"cerebrium": config_dict}

    if os.path.splitext(file)[1] != ".toml":
        file = os.path.splitext(file)[0] + ".toml"

    if os.path.exists(file):
        if not overwrite:
            cerebrium_log(
                level="WARNING",
                message="cerebrium.toml already exists. Not writing.",
                end="\t",
            )
            return None

    print(f"Saving to {file}")
    with open(file, "w") as f:
        toml.dump(config_dict, f)

    comment = (
        "# This file was automatically generated by Cerebrium as a "
        "starting point for your project. \n"
        "# You can edit it as you wish.\n"
        "# If you would like to learn more about your Cerebrium config, "
        "please visit https://docs.cerebrium.ai/cerebrium/environments/config-files#config-file-example"
    )

    # prepend comment to file
    with open(file, "r") as f:
        content = f.read()
    with open(file, "w") as f:
        f.write(f"{comment}\n\n{content}")


def load_toml(
    config_file: str, disable_confirmation: str = False, name: str = ""
) -> datatypes.CerebriumConfig:
    base_dir = os.path.dirname(config_file) or os.getcwd()

    with open(config_file, "r") as f:
        config_dict = toml.load(f)

    if "local_files" in config_dict:
        config_dict.pop("local_files")
    if "cerebrium_version" in config_dict:
        config_dict.pop("cerebrium_version")
    if "api_key" in config_dict:
        config_dict.pop("api_key")
    if "partial_upload" in config_dict:
        config_dict.pop("partial_upload")

    cerebrium_dict = config_dict.get("cerebrium", {})
    config_obj = datatypes.CerebriumConfig(
        build=datatypes.CerebriumBuild(**cerebrium_dict.get("build", {})),
        deployment=datatypes.CerebriumDeployment(
            **cerebrium_dict.get("deployment", {})
        ),
        hardware=datatypes.CerebriumHardware(**cerebrium_dict.get("hardware", {})),
        scaling=datatypes.CerebriumScaling(**cerebrium_dict.get("scaling", {})),
        dependencies=datatypes.CerebriumDependencies(
            **cerebrium_dict.get("dependencies", {})
        ),
    )
    # load in the other files and update the config
    deps = config_obj.dependencies.to_dict()
    original_deps = deps.copy()
    if os.path.exists(os.path.join(base_dir, "requirements.txt")):
        deps = update_from_file(
            os.path.join(base_dir, "requirements.txt"),
            deps,
            "pip",
            confirm=False,
        )
    if os.path.exists(os.path.join(base_dir, "pkglist.txt")):
        deps = update_from_file(
            os.path.join(base_dir, "pkglist.txt"),
            deps,
            "apt",
            confirm=False,
        )
    if os.path.exists(os.path.join(base_dir, "conda_pkglist.txt")):
        deps = update_from_file(
            os.path.join(base_dir, "conda_pkglist.txt"),
            deps,
            "conda",
            confirm=False,
        )

    if config_obj.deployment.name is None:
        config_obj.deployment.name = name if name else os.path.basename(base_dir)

    if deps:
        deps = {k: v for k, v in deps.items() if (len(v) > 0) and (v is not None)}
        original_deps = {
            k: v for k, v in original_deps.items() if (len(v) > 0) and (v is not None)
        }
        # check if there's a difference, confirm update from user if there is
        if original_deps != deps and not disable_confirmation:
            if not disable_confirmation:
                if typer.confirm(
                    colored(
                        "We've found changes in your dependencies. Would you like to update dependencies in the cerebrium.toml?",
                        "yellow",
                    )
                ):
                    config_obj.dependencies = datatypes.CerebriumDependencies(**deps)
                    save_config_to_toml_file(config_obj, config_file, overwrite=True)

    return config_obj


def load_config(
    name: str, config_file: str, disable_confirmation: bool = False
) -> datatypes.CerebriumConfig:
    """
    Loads in the toml config
    If any of the other files exist, they are also loaded in. They are then used to update the config if the user confirms.
    """

    base_dir = os.path.dirname(config_file)

    if os.path.exists(config_file):
        if config_file.endswith(".yaml") or config_file.endswith(".yml"):
            config = yaml.safe_load(open(config_file, "r"))
            config = legacy_to_toml_structure(
                name=name,
                legacy_config=config,
                config_file=config_file,
                save_to_file=False,
                disable_confirmation=disable_confirmation,
            )
        else:
            # load toml
            config = load_toml(
                config_file, disable_confirmation=disable_confirmation, name=name
            )
    else:
        # try load from toml
        config_toml_file = os.path.join(base_dir, "cerebrium.toml")
        if os.path.exists(config_toml_file):
            config = load_toml(
                config_toml_file, disable_confirmation=disable_confirmation, name=name
            )
        else:
            # try load from yaml
            config_yaml_file = os.path.join(base_dir, "config.yaml")
            if os.path.exists(config_yaml_file):
                cerebrium_log(
                    level="WARNING",
                    message=f"Could not find {config_file}, reverting to legacy config.yaml",
                    end=" ",
                )
                config = yaml.safe_load(open(config_yaml_file, "r"))
                config = legacy_to_toml_structure(
                    name=name,
                    legacy_config=config,
                    config_file=config_yaml_file,
                    save_to_file=False,
                    disable_confirmation=disable_confirmation,
                )
            else:
                cerebrium_log(
                    level="ERROR",
                    message=f"Could not find {config_file}. Please create it and try again.",
                )

    return config


def parse_requirements(file: str):
    """Takes a pip requirements file or a pkglist file and returns a list of packages"""
    if not os.path.exists(file):
        cerebrium_log(
            level="ERROR",
            message=f"Could not find {file}. Please create it and try again.",
        )
    with open(file, "r") as f:
        requirements = f.read()
    requirements_list = requirements.split("\n")
    requirements_list = [r.strip() for r in requirements_list]

    # ignore comments
    requirements_list = [r for r in requirements_list if not r.startswith("#")]
    # remove empty lines
    requirements_list = [r for r in requirements_list if r != ""]

    # if there's version numbers, we return a dict of package: version
    # otherwise we return a list of packages
    requirements_dict = req_list_to_dict(requirements_list)
    return requirements_dict


def req_list_to_dict(requirements: List[str]) -> Dict[str, str]:
    """Takes a list of requirements and returns a dict of package: version"""
    requirements_dict: Dict[str, str] = {}
    if len(requirements) == 0:
        return requirements_dict
    for r in requirements:
        # find on "==" or ">=" or "<=" or "~=" or "!=" or ">" or "<"
        search = re.search(r"==|>=|<=|~=|!=|>|<", r)
        if search is None:
            package, version = r, "latest"
        else:
            idx = search.start()
            package, version = r[:idx], r[idx:]
        requirements_dict[package] = version
    return requirements_dict


def req_dict_to_str_list(
    requirements: RequirementsType, for_display: bool = False
) -> List[str]:
    """Takes a dict of requirements and returns a list of requirements to be written to a file"""
    reqs: List[str] = []
    # if version starts with ==, >=, <=, ~=, !=, >, <, we don't add the ==
    # find >=, <=, ~=, !=, >, <
    pattern = re.compile(r"==|>=|<=|~=|!=|>|<")
    if isinstance(requirements, list):
        requirements = req_list_to_dict(requirements)
    for package, version in requirements.items():
        if str(version).lower() == "latest" and not for_display:
            version = ""
        if pattern.search(version):
            reqs.append(f"{package}{version}\n")
        else:
            if version == "":
                reqs.append(f"{package}\n")
            else:
                version = version.strip("=")
                if version.startswith("git+"):
                    reqs.append(f"{version}\n")
                else:
                    reqs.append(f"{package}=={version}\n")

    return reqs


def requirements_to_file(requirements: RequirementsType, file: str) -> None:
    """Takes a dict/list of requirements and writes them to a file"""
    reqs = req_dict_to_str_list(requirements)
    with open(file, "w") as f:
        f.writelines(reqs)


def update_from_file(
    file: str,
    toml_requirements: Dict[str, Dict[str, str]],
    key: str,
    confirm: bool = False,
) -> Dict[str, Dict[str, str]]:
    """Update the requirements dictionary from a file"""
    new_requirements = parse_requirements(file)

    if new_requirements != toml_requirements.get(key):
        if confirm:
            if typer.confirm(
                colored(
                    f"Update {key} requirements in the cerebrium.toml?",
                    "yellow",
                )
            ):
                toml_requirements[key] = new_requirements
            else:
                return toml_requirements
        else:
            toml_requirements[key] = new_requirements

    return toml_requirements
