import enum
import json
from typing import Union
from dataclasses import dataclass

MAX_MEMORY = 256
MAX_GPU_COUNT = 8
MAX_CPU = 48

MIN_CPU = 1
MIN_MEMORY = 2

DEFAULT_COOLDOWN = 60
DEFAULT_CPU = 2
DEFAULT_MEMORY = 16
DEFAULT_MIN_REPLICAS = 0
DEFAULT_MAX_REPLICAS = None
DEFAULT_GPU_SELECTION = "AMPERE_A5000"
DEFAULT_PYTHON_VERSION = "3.10"
DEFAULT_GPU_COUNT = 1
DEFAULT_CUDA_VERSION = "12"

DEFAULT_INCLUDE = "[./*, main.py]"
DEFAULT_EXCLUDE = "[./.*, ./__*]"


class PythonVersion(enum.Enum):
    PYTHON_3_8 = "3.8"
    PYTHON_3_9 = "3.9"
    PYTHON_3_10 = "3.10"
    PYTHON_3_11 = "3.11"
    PYTHON_3_12 = "3.12"


@dataclass
class HardwareOption:
    def __init__(
        self,
        name: str,
        VRAM: int,
        gpu_model: str,
        max_memory: float = 128.0,
        max_cpu: int = 36,
        max_gpu_count: int = MAX_GPU_COUNT,
        has_nvlink: bool = False,
    ):
        self.name = name
        self.gpu_model = gpu_model
        self.max_memory = max_memory
        self.max_cpu = max_cpu
        self.max_gpu_count = max_gpu_count
        self.VRAM = VRAM
        self.has_nvlink = has_nvlink

    def validate(self, cpu: int, memory: float, gpu_count: int) -> str:
        message = ""
        if cpu > self.max_cpu:
            message += f"CPU must be at most {self.max_cpu} for {self.name}.\n"
        if cpu < MIN_CPU:
            message += f"CPU must be at least {MIN_CPU} for {self.name}.\n"
        if memory > self.max_memory:
            message += f"Memory must be at most {self.max_memory} GB"
            "for {self.name}.\n"
        if memory < MIN_MEMORY:
            message += f"Memory must be at least {MIN_MEMORY} GB"
            " for {self.name}.\n"
        if gpu_count > self.max_gpu_count:
            message += f"Number of GPUs must be at most {self.max_gpu_count}"
            " for {self.name}.\n"
        if gpu_count < 1:
            message += f"Number of GPUs must be at least 1 for {self.name}.\n"

        return message

    def __str__(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=False)


class Hardware:
    GPU: HardwareOption = HardwareOption(
        name="TURING_4000", VRAM=8, gpu_model="Quadro RTX 4000"
    )
    TURING_4000: HardwareOption = HardwareOption(
        name="TURING_4000", VRAM=8, gpu_model="Quadro RTX 4000"
    )
    TURING_5000: HardwareOption = HardwareOption(
        name="TURING_5000", VRAM=8, gpu_model="RTX 5000"
    )
    AMPERE_A4000: HardwareOption = HardwareOption(
        name="AMPERE_A4000", VRAM=16, gpu_model="RTX A4000"
    )
    AMPERE_A5000: HardwareOption = HardwareOption(
        name="AMPERE_A5000", VRAM=24, gpu_model="RTX A5000"
    )
    AMPERE_A6000: HardwareOption = HardwareOption(
        name="AMPERE_A6000",
        max_memory=256.0,
        max_cpu=48,
        VRAM=48,
        gpu_model="RTX A6000",
    )
    AMPERE_A100: HardwareOption = HardwareOption(
        name="AMPERE_A100",
        max_memory=256.0,
        max_cpu=48,
        VRAM=80,
        has_nvlink=True,
        gpu_model="A100",
    )
    AMPERE_A100_40GB: HardwareOption = HardwareOption(
        name="AMPERE_A100_40GB",
        max_memory=256.0,
        max_cpu=48,
        VRAM=40,
        has_nvlink=True,
        gpu_model="A100 40GB",
    )

    @classmethod
    def available_hardware(cls):
        return list(cls.__annotations__.keys())


class CerebriumScaling:
    def __init__(
        self,
        min_replicas: int = DEFAULT_MIN_REPLICAS,
        max_replicas: Union[int, None] = DEFAULT_MAX_REPLICAS,
        cooldown: int = DEFAULT_COOLDOWN,
    ):
        self.min_replicas = min_replicas
        self.max_replicas = max_replicas
        self.cooldown = cooldown

    def __str__(self):
        return json.dumps(self.__to_dict__(), indent=4, sort_keys=False)

    def __to_dict__(self):
        return self.__dict__

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


class CerebriumBuild:
    def __init__(
        self,
        predict_data: Union[str, None] = None,
        force_rebuild=False,
        hide_public_endpoint=False,
        disable_animation=False,
        disable_build_logs=False,
        disable_syntax_check=False,
        disable_predict=False,
        disable_confirmation=False,
        init_debug=False,
        log_level="INFO",
    ):
        self.predict_data = predict_data
        self.force_rebuild = force_rebuild
        self.hide_public_endpoint = hide_public_endpoint
        self.disable_animation = disable_animation
        self.disable_build_logs = disable_build_logs
        self.disable_syntax_check = disable_syntax_check
        self.disable_predict = disable_predict
        self.init_debug = init_debug
        self.log_level = log_level
        self.disable_confirmation = disable_confirmation

    def __str__(self):
        return json.dumps(self.__to_dict__(), indent=4, sort_keys=False)

    def __to_dict__(self):
        return self.__dict__

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


class CerebriumDeployment:
    def __init__(
        self,
        name: str = "",
        python_version: str = DEFAULT_PYTHON_VERSION,
        include: str = DEFAULT_INCLUDE,
        exclude: str = DEFAULT_EXCLUDE,
        cuda_version: str = DEFAULT_CUDA_VERSION,
    ):
        self.name = name
        self.python_version = python_version
        self.include = include
        self.exclude = exclude
        self.cuda_version = cuda_version

    def __str__(self):
        return json.dumps(self.__to_dict__(), indent=4, sort_keys=False)

    def __to_dict__(self):
        return self.__dict__

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


class CerebriumHardware:
    def __init__(
        self,
        gpu: str = DEFAULT_GPU_SELECTION,
        cpu: int = DEFAULT_CPU,
        memory: float = DEFAULT_MEMORY,
        gpu_count: int = DEFAULT_GPU_COUNT,
    ):
        self.gpu = gpu
        self.cpu = cpu
        self.memory = memory
        self.gpu_count = gpu_count

    def __str__(self):
        return json.dumps(self.__to_dict__(), indent=4, sort_keys=False)

    def __to_dict__(self):
        return self.__dict__

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


class CerebriumDependencies:
    def __init__(
        self,
        pip: dict = {},
        conda: dict = {},
        apt: list = [],
    ):
        self.pip = pip
        self.conda = conda
        self.apt = apt

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4, sort_keys=False)

    def to_dict(self):
        return self.__dict__


class CerebriumConfig:
    def __init__(
        self,
        scaling: CerebriumScaling = CerebriumScaling(),
        build: CerebriumBuild = CerebriumBuild(),
        deployment: CerebriumDeployment = CerebriumDeployment(),
        hardware: CerebriumHardware = CerebriumHardware(),
        dependencies: CerebriumDependencies = CerebriumDependencies(),
        local_files: list = [],
        cerebrium_version: str = "",
        api_key: str = "",
        partial_upload=False,
    ):
        self.scaling = scaling
        self.build = build
        self.deployment = deployment
        self.hardware = hardware
        self.dependencies = dependencies
        self.local_files = local_files
        self.cerebrium_version = cerebrium_version
        self.api_key = api_key
        self.partial_upload = partial_upload

    def get(self, key, default=None):
        return self.__dict__.get(key, default)

    def __str__(self):
        # Convert to dict. All the nested classes need to be converted to dict
        # before converting to string
        dictified = self.to_dict()
        return json.dumps(dictified, indent=4, sort_keys=False)

    def to_dict(self):
        dictified = self.__dict__.copy()
        for key, value in dictified.items():
            if hasattr(value, "__dict__"):
                dictified[key] = value.__dict__
        return dictified

    def __to_json__(self):
        return json.dumps(self.to_dict())
