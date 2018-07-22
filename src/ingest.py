import os
import pandas as pd
import zipfile


class IngestData(object):

    @staticmethod
    def ingest_csv_from_zipfile(zip_file_dir: str, csv_file_name: str) -> pd.DataFrame:
        """
        Ingest the csv file from the zipfile as DataFrame
        :param zip_file_dir: Directory of zipfile
        :param csv_file_name: csv file name
        :return: DataFrame of the csv
        """

        with zipfile.ZipFile(zip_file_dir) as zip_files:
            with zip_files.open(csv_file_name) as csv_table:
                csv_df = IngestData.ingest_csv(csv_table)
        return csv_df

    @staticmethod
    def ingest_csv(csv_file_dir, index_col=False, **kwargs):
        """

        :param csv_file_dir:
        :param index_col:
        :param kwargs:
        :return:
        """
        csv_df = pd.read_csv(csv_file_dir, index_col=index_col, **kwargs)
        return csv_df

