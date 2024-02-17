from napalm.package.detector_info import DetectorInfo, CompetitionInfo
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification


def into_detector_info(slither_detector: AbstractDetector) -> DetectorInfo:
    severity = slither_detector.IMPACT
    match severity:
        case DetectorClassification.HIGH:
            severity = "HIGH"
        case DetectorClassification.MEDIUM:
            severity = "MEDIUM"
        case DetectorClassification.LOW:
            severity = "LOW"
        case DetectorClassification.INFORMATIONAL:
            severity = "INFO"
        case DetectorClassification.OPTIMIZATION:
            severity = "OPTIMIZATION"
        case _:
            severity = "unknown"

    competitors = (
        [
            CompetitionInfo(
                name=competitor.get("name"),
                title=competitor.get("title"),
            )
            for competitor in slither_detector.COMPETITORS
        ]
        if hasattr(slither_detector, "COMPETITORS")
        else []
    )

    return DetectorInfo(
        id=slither_detector.ARGUMENT or slither_detector.__name__,
        name=slither_detector.ARGUMENT or slither_detector.__name__,
        short_description=slither_detector.HELP or "No description available",
        long_description=slither_detector.HELP or "No description available",
        severity=severity,
        base=slither_detector,
        twins=[] if not hasattr(slither_detector, "TWINS") else slither_detector.TWINS,
        false_positive_prompt=(
            slither_detector.FALSE_POSITIVE_PROMPT
            if hasattr(slither_detector, "FALSE_POSITIVE_PROMPT")
            else None
        ),
        competitors=competitors,
    )
