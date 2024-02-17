import inspect
from importlib import resources
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
from typing import Optional

import click
from napalm.package.collection import Collection
from napalm.package.detector_info import DetectorInfo
from napalm.plugins.base import ToolPlugin
from napalm.tool.tool_runner import ToolRunner
from slither.detectors.abstract_detector import AbstractDetector

from napalm_slither.detector_info import into_detector_info
from napalm_slither.init import setup_sample_detectors
from napalm_slither.slither_modules import (
    slither_collection,
)
from napalm_slither.slither_tool_runner import SlitherToolRunner


class SlitherPlugin(ToolPlugin):
    def tool_name(self) -> str:
        return "slither"

    def tool_runner(self) -> Optional[ToolRunner]:
        return SlitherToolRunner()

    def base_collection(self) -> Optional[Collection]:
        return slither_collection()

    def discover_modules(self, anchor):
        with resources.as_file(anchor) as module_directory:
            for file in module_directory.rglob("*.py"):
                spec = spec_from_file_location(file.name, file)
                module = module_from_spec(spec)

                spec.loader.exec_module(module)

                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if attribute_name == "AbstractDetector":
                        continue

                    if inspect.isclass(attribute) and issubclass(
                        attribute, AbstractDetector
                    ):
                        if attribute.__module__ != module.__name__:
                            continue

                        yield attribute

    def detector_info(self, slither_detector: AbstractDetector) -> DetectorInfo:
        return into_detector_info(slither_detector)

    def initialize_default_files(self, module: Path):
        setup_sample_detectors(module)

    def instrument_command(self, command):
        click.option(
            "--slither-arguments", help="Arguments to pass to slither", type=str
        )(command)
        return command
