from typing import List
from slither.utils.output import Output
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification


class SampleDetector(AbstractDetector):
    """
    Sample detector for napalm
    """

    ARGUMENT = 'napalm-sample-detector'
    HELP = 'This is a sample detector for napalm'
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.HIGH

    def _detect(self) -> List[Output]:
        return [self.generate_result(["Sample finding"])]
