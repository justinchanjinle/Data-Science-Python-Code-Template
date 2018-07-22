import os


def join_dir(*dir) -> str:
    """
    Joins multiple paths
    :param dir: Directories separated by comma
    :return: Joined directory
    """
    return os.path.join(*dir)


def get_parent_dir(path: str) -> str:
    """
    Returns parent directory of the path
    :param path: Selected path
    :return: Parent directory of selected path
    """
    return os.path.dirname(path)


def get_abs_dir(path: str) -> str:
    """
    Returns absolute path
    :param path: Selected path
    :return: Absolute path of selected path
    """
    return os.path.abspath(path)
