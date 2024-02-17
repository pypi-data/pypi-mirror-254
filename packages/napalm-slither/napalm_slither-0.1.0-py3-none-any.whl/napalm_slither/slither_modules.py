import inspect
from typing import List, Type

import slither.detectors.all_detectors as all_detectors
from napalm.package.collection import Collection
from slither.detectors.abstract_detector import AbstractDetector
from toolz.curried import filter, map, pipe


def base_slither_detectors() -> List[Type[AbstractDetector]]:
    return pipe(
        all_detectors,
        dir,
        map(lambda name: getattr(all_detectors, name)),
        filter(inspect.isclass),
        filter(lambda d: issubclass(d, AbstractDetector)),
        list,
    )


def slither_collection() -> Collection:
    slither_base_collection = Collection(
        collection_name="detectors",
        package_name="slither",
        semgrep_configurations=[],
        plugin_detectors={"slither": base_slither_detectors()},
    )
    return slither_base_collection
