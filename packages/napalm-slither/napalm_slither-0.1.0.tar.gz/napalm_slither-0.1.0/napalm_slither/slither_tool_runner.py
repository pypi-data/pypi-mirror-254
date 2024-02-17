import subprocess

from loguru import logger
from napalm.tool.tool_runner import ToolRunner
from pydantic_sarif.model import (
    StaticAnalysisResultsFormatSarifVersion210JsonSchema as Report,
)

from napalm_slither.environment_setter import EnvironmentSetter
from napalm_slither.slither_modules import base_slither_detectors


class SlitherToolRunner(ToolRunner):
    @staticmethod
    def _slither_base_exclusion_args():
        detectors = base_slither_detectors()
        return ["--exclude", ",".join([detector.ARGUMENT for detector in detectors])]

    def run_analysis(self, target, workflow, collections, **kwargs):
        with EnvironmentSetter("NAPALM_WORKFLOW", workflow):
            _base = "slither/detectors" in [
                collection.full_name for collection in collections
            ]
            return self._run_analysis(
                target=target,
                slither_arguments=kwargs.get("slither_arguments", []),
                slither_base_collection=_base,
            )

    def _run_analysis(self, target, slither_arguments, slither_base_collection):
        exclusion_args = (
            self._slither_base_exclusion_args() if not slither_base_collection else []
        )
        additional_args = slither_arguments.split(" ") if slither_arguments else []
        command = (
            ["slither", "--sarif", "-"] + additional_args + exclusion_args + [target]
        )
        # print(" ".join(command))
        result = subprocess.run(command, capture_output=True, text=True)

        if result.stderr:
            logger.debug(f"Slither Logs: \n{result.stderr}")

        try:
            sarif_result = Report.model_validate_json(result.stdout)
        except Exception as e:
            logger.error(f"Error parsing slither output", error=e)
            print("Try running command locally:")
            print(" ".join(command))
            return None

        return sarif_result
