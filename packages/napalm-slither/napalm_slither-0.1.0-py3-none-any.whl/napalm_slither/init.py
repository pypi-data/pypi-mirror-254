from pathlib import Path


def setup_sample_detectors(module: Path):
    # detectors / indicators / optimisations are already initialised

    sample_directory = (
        Path(__file__).parent.parent / "templates" / "init"
    )

    slither_file = (module / "detectors") / "slither_sample_detector.py"
    slither_template = sample_directory / "example_slither_module.py"

    slither_file.write_text(slither_template.read_text())
