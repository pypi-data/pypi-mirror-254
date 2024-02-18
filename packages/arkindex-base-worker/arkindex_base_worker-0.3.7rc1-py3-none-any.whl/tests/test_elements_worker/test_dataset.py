import json
import logging

import pytest
from apistar.exceptions import ErrorResponse

from arkindex_worker.models import Dataset
from arkindex_worker.worker.dataset import DatasetState
from tests.conftest import PROCESS_ID
from tests.test_elements_worker import BASE_API_CALLS


def test_list_process_datasets_readonly_error(mock_dataset_worker):
    # Set worker in read_only mode
    mock_dataset_worker.worker_run_id = None
    assert mock_dataset_worker.is_read_only

    with pytest.raises(
        AssertionError, match="This helper is not available in read-only mode."
    ):
        mock_dataset_worker.list_process_datasets()


def test_list_process_datasets_api_error(responses, mock_dataset_worker):
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/",
        status=500,
    )

    with pytest.raises(
        Exception, match="Stopping pagination as data will be incomplete"
    ):
        next(mock_dataset_worker.list_process_datasets())

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # The API call is retried 5 times
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
    ]


def test_list_process_datasets(
    responses,
    mock_dataset_worker,
):
    expected_results = [
        {
            "id": "dataset_1",
            "name": "Dataset 1",
            "description": "My first great dataset",
            "sets": ["train", "val", "test"],
            "state": "open",
            "corpus_id": "corpus_id",
            "creator": "test@teklia.com",
            "task_id": "task_id_1",
        },
        {
            "id": "dataset_2",
            "name": "Dataset 2",
            "description": "My second great dataset",
            "sets": ["train", "val"],
            "state": "complete",
            "corpus_id": "corpus_id",
            "creator": "test@teklia.com",
            "task_id": "task_id_2",
        },
        {
            "id": "dataset_3",
            "name": "Dataset 3 (TRASHME)",
            "description": "My third dataset, in error",
            "sets": ["nonsense", "random set"],
            "state": "error",
            "corpus_id": "corpus_id",
            "creator": "test@teklia.com",
            "task_id": "task_id_3",
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/",
        status=200,
        json={
            "count": 3,
            "next": None,
            "results": expected_results,
        },
    )

    for idx, dataset in enumerate(mock_dataset_worker.list_process_datasets()):
        assert isinstance(dataset, Dataset)
        assert dataset == expected_results[idx]

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
    ]


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # Dataset
        (
            {"dataset": None},
            "dataset shouldn't be null and should be a Dataset",
        ),
        (
            {"dataset": "not Dataset type"},
            "dataset shouldn't be null and should be a Dataset",
        ),
    ],
)
def test_list_dataset_elements_wrong_param_dataset(mock_dataset_worker, payload, error):
    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.list_dataset_elements(**payload)


def test_list_dataset_elements_api_error(
    responses, mock_dataset_worker, default_dataset
):
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/",
        status=500,
    )

    with pytest.raises(
        Exception, match="Stopping pagination as data will be incomplete"
    ):
        next(mock_dataset_worker.list_dataset_elements(dataset=default_dataset))

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # The API call is retried 5 times
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
    ]


def test_list_dataset_elements(
    responses,
    mock_dataset_worker,
    default_dataset,
):
    expected_results = [
        {
            "set": "set_1",
            "element": {
                "id": "0000",
                "type": "page",
                "name": "Test",
                "corpus": {},
                "thumbnail_url": None,
                "zone": {},
                "best_classes": None,
                "has_children": None,
                "worker_version_id": None,
                "worker_run_id": None,
            },
        },
        {
            "set": "set_1",
            "element": {
                "id": "1111",
                "type": "page",
                "name": "Test 2",
                "corpus": {},
                "thumbnail_url": None,
                "zone": {},
                "best_classes": None,
                "has_children": None,
                "worker_version_id": None,
                "worker_run_id": None,
            },
        },
        {
            "set": "set_2",
            "element": {
                "id": "2222",
                "type": "page",
                "name": "Test 3",
                "corpus": {},
                "thumbnail_url": None,
                "zone": {},
                "best_classes": None,
                "has_children": None,
                "worker_version_id": None,
                "worker_run_id": None,
            },
        },
        {
            "set": "set_3",
            "element": {
                "id": "3333",
                "type": "page",
                "name": "Test 4",
                "corpus": {},
                "thumbnail_url": None,
                "zone": {},
                "best_classes": None,
                "has_children": None,
                "worker_version_id": None,
                "worker_run_id": None,
            },
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/",
        status=200,
        json={
            "count": 4,
            "next": None,
            "results": expected_results,
        },
    )

    for idx, element in enumerate(
        mock_dataset_worker.list_dataset_elements(dataset=default_dataset)
    ):
        assert element == (
            expected_results[idx]["set"],
            expected_results[idx]["element"],
        )

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
    ]


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # Dataset
        (
            {"dataset": None},
            "dataset shouldn't be null and should be a Dataset",
        ),
        (
            {"dataset": "not dataset type"},
            "dataset shouldn't be null and should be a Dataset",
        ),
    ],
)
def test_update_dataset_state_wrong_param_dataset(
    mock_dataset_worker, default_dataset, payload, error
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
        **payload,
    }

    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.update_dataset_state(**api_payload)


@pytest.mark.parametrize(
    ("payload", "error"),
    [
        # DatasetState
        (
            {"state": None},
            "state shouldn't be null and should be a str from DatasetState",
        ),
        (
            {"state": "not dataset type"},
            "state shouldn't be null and should be a str from DatasetState",
        ),
    ],
)
def test_update_dataset_state_wrong_param_state(
    mock_dataset_worker, default_dataset, payload, error
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
        **payload,
    }

    with pytest.raises(AssertionError, match=error):
        mock_dataset_worker.update_dataset_state(**api_payload)


def test_update_dataset_state_readonly_error(
    caplog, mock_dev_dataset_worker, default_dataset
):
    api_payload = {
        "dataset": Dataset(**default_dataset),
        "state": DatasetState.Building,
    }

    assert not mock_dev_dataset_worker.update_dataset_state(**api_payload)
    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (
            logging.WARNING,
            "Cannot update dataset as this worker is in read-only mode",
        ),
    ]


def test_update_dataset_state_api_error(
    responses, mock_dataset_worker, default_dataset
):
    responses.add(
        responses.PATCH,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=500,
    )

    with pytest.raises(ErrorResponse):
        mock_dataset_worker.update_dataset_state(
            dataset=default_dataset,
            state=DatasetState.Building,
        )

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # We retry 5 times the API call
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
    ]


def test_update_dataset_state(
    responses,
    mock_dataset_worker,
    default_dataset,
):
    dataset_response = {
        "name": "My dataset",
        "description": "A super dataset built by me",
        "sets": ["set_1", "set_2", "set_3"],
        "state": DatasetState.Building.value,
    }
    responses.add(
        responses.PATCH,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=200,
        json=dataset_response,
    )

    updated_dataset = mock_dataset_worker.update_dataset_state(
        dataset=default_dataset,
        state=DatasetState.Building,
    )

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        (
            "PATCH",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        ),
    ]
    assert json.loads(responses.calls[-1].request.body) == {
        "state": DatasetState.Building.value
    }
    assert updated_dataset == Dataset(**{**default_dataset, **dataset_response})
