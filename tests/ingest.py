import pytest

from src.ingest import IngestData
from tests.enumerations import TestDirectories, TestFileNames


def test_ingest_csv_from_zipfile():

    try:

        adult_data_df = IngestData.ingest_csv_from_zipfile(TestDirectories.ZIP_FILE_DIR.value,
                                                           TestFileNames.ZIP_CSV_FILE_NAME.value)

    except Exception as exception:

        pytest.fail('Ingest zip file error: {}'.format(exception))

    pass


def test_ingest_csv():

    try:

        school_data_df = IngestData.ingest_csv(TestDirectories.CSV_FILE_DIR.value)

    except Exception as exception:

        pytest.fail('Ingest zip file error: {}'.format(exception))

    pass