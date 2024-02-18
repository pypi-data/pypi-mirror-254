"""
BaseWorker methods for datasets.
"""

from collections.abc import Iterator
from enum import Enum

from arkindex_worker import logger
from arkindex_worker.models import Dataset, Element


class DatasetState(Enum):
    """
    State of a dataset.
    """

    Open = "open"
    """
    The dataset is open.
    """

    Building = "building"
    """
    The dataset is being built.
    """

    Complete = "complete"
    """
    The dataset is complete.
    """

    Error = "error"
    """
    The dataset is in error.
    """


class DatasetMixin:
    def list_process_datasets(self) -> Iterator[Dataset]:
        """
        List datasets associated to the worker's process. This helper is not available in developer mode.

        :returns: An iterator of ``Dataset`` objects built from the ``ListProcessDatasets`` API endpoint.
        """
        assert not self.is_read_only, "This helper is not available in read-only mode."

        results = self.api_client.paginate(
            "ListProcessDatasets", id=self.process_information["id"]
        )

        return map(Dataset, list(results))

    def list_dataset_elements(self, dataset: Dataset) -> Iterator[tuple[str, Element]]:
        """
        List elements in a dataset.

        :param dataset: Dataset to find elements in.
        :returns: An iterator of tuples built from the ``ListDatasetElements`` API endpoint.
        """
        assert dataset and isinstance(
            dataset, Dataset
        ), "dataset shouldn't be null and should be a Dataset"

        results = self.api_client.paginate("ListDatasetElements", id=dataset.id)

        def format_result(result):
            return (result["set"], Element(**result["element"]))

        return map(format_result, list(results))

    def update_dataset_state(self, dataset: Dataset, state: DatasetState) -> Dataset:
        """
        Partially updates a dataset state through the API.

        :param dataset: The dataset to update.
        :param state: State of the dataset.
        :returns: The updated ``Dataset`` object from the ``PartialUpdateDataset`` API endpoint.
        """
        assert dataset and isinstance(
            dataset, Dataset
        ), "dataset shouldn't be null and should be a Dataset"
        assert state and isinstance(
            state, DatasetState
        ), "state shouldn't be null and should be a str from DatasetState"

        if self.is_read_only:
            logger.warning("Cannot update dataset as this worker is in read-only mode")
            return

        updated_dataset = self.request(
            "PartialUpdateDataset",
            id=dataset.id,
            body={"state": state.value},
        )
        dataset.update(updated_dataset)

        return dataset
