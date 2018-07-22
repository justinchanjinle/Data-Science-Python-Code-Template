from enum import Enum

from utils.helpers import join_dir, get_parent_dir, get_abs_dir


class TestFileNames(Enum):
    ZIP_FILE_NAME = 'adult-income-dataset.zip'
    ZIP_CSV_FILE_NAME = 'adult.csv'
    CSV_FILE_NAME = '2016-school-explorers.csv'


class TestDirectories(Enum):

    ZIP_FILE_DIR = join_dir(get_parent_dir(get_parent_dir(get_abs_dir(__file__))), 'data',
                            TestFileNames.ZIP_FILE_NAME.value)

    CSV_FILE_DIR = join_dir(get_parent_dir(get_parent_dir(get_abs_dir(__file__))), 'data',
                            TestFileNames.CSV_FILE_NAME.value)
