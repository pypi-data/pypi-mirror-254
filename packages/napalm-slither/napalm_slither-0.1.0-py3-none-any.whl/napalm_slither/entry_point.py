import os

from loguru import logger
from napalm.package.collection_manager import CollectionManager
from napalm.storage import WorkflowStorage, get_storage_provider


def napalm_entry_point_slither():
    """Returns a list of slither modules

    Napalm acts as an intermediary between slither plugins in napalm packages and slither. Unexpectedly, perhaps,
    this makes napalm itself the detector plugin for slither.

    This function uses the environment variable NAPALM_WORKFLOW ( as set by the code in napalm/cli/run.py ) to determine
    which collections to load.
    """
    logger.info("napalm_entry_point_slithers")
    modules = []

    # get the current workflow
    workflow = os.environ.get("NAPALM_WORKFLOW", None)

    if workflow is None:
        # slither wasn't ran by napalm
        return [], []

    # get the collection manager
    get_storage_provider("pickle")
    workflow_storage = WorkflowStorage(get_storage_provider("pickle"))
    workflow_collections = workflow_storage.get_workflow(workflow)

    if workflow_collections is None or workflow_collections is []:
        logger.info(f"Workflow {workflow} does not exist")
        return [], []

    collection_manager = CollectionManager()
    for collection_name in workflow_collections:
        collection = collection_manager.get(collection_name)
        if collection.full_name == "slither/detectors":
            continue
        modules += collection.plugin_detectors.get("slither", [])

    return modules, []
