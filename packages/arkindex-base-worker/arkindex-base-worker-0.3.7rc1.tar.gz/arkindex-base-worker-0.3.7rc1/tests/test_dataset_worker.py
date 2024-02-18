import logging

import pytest
from apistar.exceptions import ErrorResponse

from arkindex_worker.worker import MissingDatasetArchive
from arkindex_worker.worker.dataset import DatasetState
from tests.conftest import FIXTURES_DIR, PROCESS_ID
from tests.test_elements_worker import BASE_API_CALLS


def test_download_dataset_artifact_list_api_error(
    responses, mock_dataset_worker, default_dataset
):
    task_id = default_dataset.task_id

    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifacts/",
        status=500,
    )

    with pytest.raises(ErrorResponse):
        mock_dataset_worker.download_dataset_artifact(default_dataset)

    assert len(responses.calls) == len(BASE_API_CALLS) + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        # The API call is retried 5 times
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
    ]


def test_download_dataset_artifact_download_api_error(
    responses, mock_dataset_worker, default_dataset
):
    task_id = default_dataset.task_id

    expected_results = [
        {
            "id": "artifact_1",
            "path": "dataset_id.tar.zst",
            "size": 42,
            "content_type": "application/zstd",
            "s3_put_url": None,
            "created": "2000-01-01T00:00:00Z",
            "updated": "2000-01-01T00:00:00Z",
        },
        {
            "id": "artifact_2",
            "path": "logs.log",
            "size": 42,
            "content_type": "text/plain",
            "s3_put_url": None,
            "created": "2000-01-01T00:00:00Z",
            "updated": "2000-01-01T00:00:00Z",
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifacts/",
        status=200,
        json=expected_results,
    )
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst",
        status=500,
    )

    with pytest.raises(ErrorResponse):
        mock_dataset_worker.download_dataset_artifact(default_dataset)

    assert len(responses.calls) == len(BASE_API_CALLS) + 6
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        # The API call is retried 5 times
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
    ]


def test_download_dataset_artifact_no_archive(
    responses, mock_dataset_worker, default_dataset
):
    task_id = default_dataset.task_id

    expected_results = [
        {
            "id": "artifact_id",
            "path": "logs.log",
            "size": 42,
            "content_type": "text/plain",
            "s3_put_url": None,
            "created": "2000-01-01T00:00:00Z",
            "updated": "2000-01-01T00:00:00Z",
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifacts/",
        status=200,
        json=expected_results,
    )

    with pytest.raises(
        MissingDatasetArchive,
        match="The dataset compressed archive artifact was not found.",
    ):
        mock_dataset_worker.download_dataset_artifact(default_dataset)

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
    ]


def test_download_dataset_artifact(
    mocker, tmp_path, responses, mock_dataset_worker, default_dataset
):
    task_id = default_dataset.task_id
    archive_path = (
        FIXTURES_DIR
        / "extract_parent_archives"
        / "first_parent"
        / "arkindex_data.tar.zst"
    )
    mocker.patch(
        "arkindex_worker.worker.base.BaseWorker.find_extras_directory",
        return_value=tmp_path,
    )

    expected_results = [
        {
            "id": "artifact_1",
            "path": "dataset_id.tar.zst",
            "size": 42,
            "content_type": "application/zstd",
            "s3_put_url": None,
            "created": "2000-01-01T00:00:00Z",
            "updated": "2000-01-01T00:00:00Z",
        },
        {
            "id": "artifact_2",
            "path": "logs.log",
            "size": 42,
            "content_type": "text/plain",
            "s3_put_url": None,
            "created": "2000-01-01T00:00:00Z",
            "updated": "2000-01-01T00:00:00Z",
        },
    ]
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifacts/",
        status=200,
        json=expected_results,
    )
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst",
        status=200,
        body=archive_path.read_bytes(),
        content_type="application/zstd",
    )

    archive = mock_dataset_worker.download_dataset_artifact(default_dataset)
    assert archive == tmp_path / "dataset_id.tar.zst"
    assert archive.read_bytes() == archive_path.read_bytes()
    archive.unlink()

    assert len(responses.calls) == len(BASE_API_CALLS) + 2
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{task_id}/artifact/dataset_id.tar.zst"),
    ]


def test_list_dataset_elements_per_split_api_error(
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
        mock_dataset_worker.list_dataset_elements_per_split(default_dataset)

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


def test_list_dataset_elements_per_split(
    responses, mock_dataset_worker, default_dataset
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

    assert list(
        mock_dataset_worker.list_dataset_elements_per_split(default_dataset)
    ) == [
        ("set_1", [expected_results[0]["element"], expected_results[1]["element"]]),
        ("set_2", [expected_results[2]["element"]]),
        ("set_3", [expected_results[3]["element"]]),
    ]

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        (
            "GET",
            f"http://testserver/api/v1/datasets/{default_dataset.id}/elements/?with_count=true",
        ),
    ]


def test_list_datasets_read_only(mock_dev_dataset_worker):
    assert list(mock_dev_dataset_worker.list_datasets()) == [
        "11111111-1111-1111-1111-111111111111",
        "22222222-2222-2222-2222-222222222222",
    ]


def test_list_datasets_api_error(responses, mock_dataset_worker):
    responses.add(
        responses.GET,
        f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/",
        status=500,
    )

    with pytest.raises(
        Exception, match="Stopping pagination as data will be incomplete"
    ):
        mock_dataset_worker.list_datasets()

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


def test_list_datasets(responses, mock_dataset_worker):
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

    assert list(mock_dataset_worker.list_datasets()) == expected_results

    assert len(responses.calls) == len(BASE_API_CALLS) + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS + [
        ("GET", f"http://testserver/api/v1/process/{PROCESS_ID}/datasets/"),
    ]


@pytest.mark.parametrize("generator", [True, False])
def test_run_no_datasets(mocker, caplog, mock_dataset_worker, generator):
    mocker.patch("arkindex_worker.worker.DatasetWorker.list_datasets", return_value=[])
    mock_dataset_worker.generator = generator

    with pytest.raises(SystemExit):
        mock_dataset_worker.run()

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (logging.WARNING, "No datasets to process, stopping."),
    ]


@pytest.mark.parametrize(
    ("generator", "error"),
    [
        (True, "When generating a new dataset, its state should be Open."),
        (False, "When processing an existing dataset, its state should be Complete."),
    ],
)
def test_run_initial_dataset_state_error(
    mocker, responses, caplog, mock_dataset_worker, default_dataset, generator, error
):
    default_dataset.state = DatasetState.Building.value
    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset],
    )
    mock_dataset_worker.generator = generator

    extra_call = []
    if generator:
        responses.add(
            responses.PATCH,
            f"http://testserver/api/v1/datasets/{default_dataset.id}/",
            status=200,
            json={},
        )
        extra_call = [
            ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ]

    with pytest.raises(SystemExit):
        mock_dataset_worker.run()

    assert len(responses.calls) == len(BASE_API_CALLS) * 2 + len(extra_call)
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS * 2 + extra_call

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (
            logging.WARNING,
            f"Failed running worker on dataset dataset_id: AssertionError('{error}')",
        ),
        (
            logging.ERROR,
            "Ran on 1 datasets: 0 completed, 1 failed",
        ),
    ]


def test_run_update_dataset_state_api_error(
    mocker, responses, caplog, mock_dataset_worker, default_dataset
):
    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset],
    )
    mock_dataset_worker.generator = True

    responses.add(
        responses.PATCH,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=500,
    )

    with pytest.raises(SystemExit):
        mock_dataset_worker.run()

    assert len(responses.calls) == len(BASE_API_CALLS) * 2 + 10
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS * 2 + [
        # We retry 5 times the API call to update the Dataset as Building
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        # We retry 5 times the API call to update the Dataset as in Error
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
    ]

    retries = [3.0, 4.0, 8.0, 16.0]
    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (logging.INFO, "Processing Dataset (dataset_id) (1/1)"),
        (logging.INFO, "Building Dataset (dataset_id) (1/1)"),
        *[
            (
                logging.INFO,
                f"Retrying arkindex_worker.worker.base.BaseWorker.request in {retry} seconds as it raised ErrorResponse: .",
            )
            for retry in retries
        ],
        (
            logging.WARNING,
            "An API error occurred while processing dataset dataset_id: 500 Internal Server Error - None",
        ),
        *[
            (
                logging.INFO,
                f"Retrying arkindex_worker.worker.base.BaseWorker.request in {retry} seconds as it raised ErrorResponse: .",
            )
            for retry in retries
        ],
        (
            logging.ERROR,
            "Ran on 1 datasets: 0 completed, 1 failed",
        ),
    ]


def test_run_download_dataset_artifact_api_error(
    mocker,
    tmp_path,
    responses,
    caplog,
    mock_dataset_worker,
    default_dataset,
):
    default_dataset.state = DatasetState.Complete.value

    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset],
    )
    mocker.patch(
        "arkindex_worker.worker.base.BaseWorker.find_extras_directory",
        return_value=tmp_path,
    )

    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
        status=500,
    )

    with pytest.raises(SystemExit):
        mock_dataset_worker.run()

    assert len(responses.calls) == len(BASE_API_CALLS) * 2 + 5
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS * 2 + [
        # We retry 5 times the API call
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
    ]

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (logging.INFO, "Processing Dataset (dataset_id) (1/1)"),
        (logging.INFO, "Downloading data for Dataset (dataset_id) (1/1)"),
        *[
            (
                logging.INFO,
                f"Retrying arkindex_worker.worker.base.BaseWorker.request in {retry} seconds as it raised ErrorResponse: .",
            )
            for retry in [3.0, 4.0, 8.0, 16.0]
        ],
        (
            logging.WARNING,
            "An API error occurred while processing dataset dataset_id: 500 Internal Server Error - None",
        ),
        (
            logging.ERROR,
            "Ran on 1 datasets: 0 completed, 1 failed",
        ),
    ]


def test_run_no_downloaded_artifact_error(
    mocker,
    tmp_path,
    responses,
    caplog,
    mock_dataset_worker,
    default_dataset,
):
    default_dataset.state = DatasetState.Complete.value

    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset],
    )
    mocker.patch(
        "arkindex_worker.worker.base.BaseWorker.find_extras_directory",
        return_value=tmp_path,
    )

    responses.add(
        responses.GET,
        f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
        status=200,
        json={},
    )

    with pytest.raises(SystemExit):
        mock_dataset_worker.run()

    assert len(responses.calls) == len(BASE_API_CALLS) * 2 + 1
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS * 2 + [
        ("GET", f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/"),
    ]

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (logging.INFO, "Processing Dataset (dataset_id) (1/1)"),
        (logging.INFO, "Downloading data for Dataset (dataset_id) (1/1)"),
        (
            logging.WARNING,
            "Failed running worker on dataset dataset_id: MissingDatasetArchive('The dataset compressed archive artifact was not found.')",
        ),
        (
            logging.ERROR,
            "Ran on 1 datasets: 0 completed, 1 failed",
        ),
    ]


@pytest.mark.parametrize(
    ("generator", "state"), [(True, DatasetState.Open), (False, DatasetState.Complete)]
)
def test_run(
    mocker,
    tmp_path,
    responses,
    caplog,
    mock_dataset_worker,
    default_dataset,
    default_artifact,
    generator,
    state,
):
    mock_dataset_worker.generator = generator
    default_dataset.state = state.value

    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset],
    )
    mocker.patch(
        "arkindex_worker.worker.base.BaseWorker.find_extras_directory",
        return_value=tmp_path,
    )
    mock_process = mocker.patch("arkindex_worker.worker.DatasetWorker.process_dataset")

    extra_calls = []
    extra_logs = []
    if generator:
        responses.add(
            responses.PATCH,
            f"http://testserver/api/v1/datasets/{default_dataset.id}/",
            status=200,
            json={},
        )
        extra_calls += [
            ("PATCH", f"http://testserver/api/v1/datasets/{default_dataset.id}/"),
        ] * 2
        extra_logs += [
            (logging.INFO, "Building Dataset (dataset_id) (1/1)"),
            (logging.INFO, "Completed Dataset (dataset_id) (1/1)"),
        ]
    else:
        archive_path = (
            FIXTURES_DIR
            / "extract_parent_archives"
            / "first_parent"
            / "arkindex_data.tar.zst"
        )
        responses.add(
            responses.GET,
            f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
            status=200,
            json=[default_artifact],
        )
        responses.add(
            responses.GET,
            f"http://testserver/api/v1/task/{default_dataset.task_id}/artifact/dataset_id.tar.zst",
            status=200,
            body=archive_path.read_bytes(),
            content_type="application/zstd",
        )
        extra_calls += [
            (
                "GET",
                f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
            ),
            (
                "GET",
                f"http://testserver/api/v1/task/{default_dataset.task_id}/artifact/dataset_id.tar.zst",
            ),
        ]
        extra_logs += [
            (logging.INFO, "Downloading data for Dataset (dataset_id) (1/1)"),
        ]

    mock_dataset_worker.run()

    assert mock_process.call_count == 1

    assert len(responses.calls) == len(BASE_API_CALLS) * 2 + len(extra_calls)
    assert [
        (call.request.method, call.request.url) for call in responses.calls
    ] == BASE_API_CALLS * 2 + extra_calls

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.INFO, "Loaded Worker Fake worker @ 123412 from API"),
        (logging.INFO, "Processing Dataset (dataset_id) (1/1)"),
    ] + extra_logs


@pytest.mark.parametrize(
    ("generator", "state"), [(True, DatasetState.Open), (False, DatasetState.Complete)]
)
def test_run_read_only(
    mocker,
    tmp_path,
    responses,
    caplog,
    mock_dev_dataset_worker,
    default_dataset,
    default_artifact,
    generator,
    state,
):
    mock_dev_dataset_worker.generator = generator
    default_dataset.state = state.value

    mocker.patch(
        "arkindex_worker.worker.DatasetWorker.list_datasets",
        return_value=[default_dataset.id],
    )
    mocker.patch(
        "arkindex_worker.worker.base.BaseWorker.find_extras_directory",
        return_value=tmp_path,
    )
    mock_process = mocker.patch("arkindex_worker.worker.DatasetWorker.process_dataset")

    responses.add(
        responses.GET,
        f"http://testserver/api/v1/datasets/{default_dataset.id}/",
        status=200,
        json=default_dataset,
    )

    extra_calls = []
    extra_logs = []
    if generator:
        extra_logs += [
            (logging.INFO, "Building Dataset (dataset_id) (1/1)"),
            (
                logging.WARNING,
                "Cannot update dataset as this worker is in read-only mode",
            ),
            (logging.INFO, "Completed Dataset (dataset_id) (1/1)"),
            (
                logging.WARNING,
                "Cannot update dataset as this worker is in read-only mode",
            ),
        ]
    else:
        archive_path = (
            FIXTURES_DIR
            / "extract_parent_archives"
            / "first_parent"
            / "arkindex_data.tar.zst"
        )
        responses.add(
            responses.GET,
            f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
            status=200,
            json=[default_artifact],
        )
        responses.add(
            responses.GET,
            f"http://testserver/api/v1/task/{default_dataset.task_id}/artifact/dataset_id.tar.zst",
            status=200,
            body=archive_path.read_bytes(),
            content_type="application/zstd",
        )
        extra_calls += [
            (
                "GET",
                f"http://testserver/api/v1/task/{default_dataset.task_id}/artifacts/",
            ),
            (
                "GET",
                f"http://testserver/api/v1/task/{default_dataset.task_id}/artifact/dataset_id.tar.zst",
            ),
        ]
        extra_logs += [
            (logging.INFO, "Downloading data for Dataset (dataset_id) (1/1)"),
        ]

    mock_dev_dataset_worker.run()

    assert mock_process.call_count == 1

    assert len(responses.calls) == 1 + len(extra_calls)
    assert [(call.request.method, call.request.url) for call in responses.calls] == [
        ("GET", f"http://testserver/api/v1/datasets/{default_dataset.id}/")
    ] + extra_calls

    assert [(level, message) for _, level, message in caplog.record_tuples] == [
        (logging.WARNING, "Running without any extra configuration"),
        (logging.INFO, "Processing Dataset (dataset_id) (1/1)"),
    ] + extra_logs
