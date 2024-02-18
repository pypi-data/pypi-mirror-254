import datetime
import os


def assert_is_file(path: str):
    if not os.path.isfile(path):
        raise Exception(f"not a valid file path: {path}")


def assert_is_dir(path: str):
    if not os.path.isdir(path):
        raise Exception(f"not a valid directory: {path}")


def assert_is_path(path: str):
    if not (os.path.isdir(path) or os.path.isfile(path)):
        raise Exception(f"not a valid path: {path}")


def winapi_path(path: str):
    """
    Regular DOS paths are limited to MAX_PATH (260) characters. When the size exceeds this limit,
    some python packages may raise FileNotFoundError, e.g. zipfile.ZipFile().extract().
    In such cases, wrap the path with this function will help.

    see:
    https://stackoverflow.com/questions/36219317/pathname-too-long-to-open/36237176
    """
    path = os.path.abspath(path)
    if path.startswith(u"\\\\"):
        return u"\\\\?\\UNC\\" + path[2:]
    return u"\\\\?\\" + path


def get_create_time(path: str):
    if not os.path.exists(path):
        raise Exception(f'not a valid path: {path}')
    return datetime.datetime.fromtimestamp(os.path.getctime(path))


def get_last_create_time(directory: str) -> datetime:
    """
    walk through a dir tree, return the last create time of file in it
    """
    directory = os.path.abspath(directory)
    assert_is_dir(directory)

    # the creation time of the dir must be less than those of all files in it
    ans = get_create_time(directory)
    for (root, dirs, files) in os.walk(directory, topdown=True):
        if len(files) == 0:
            continue
        ans = max(ans, max([get_create_time(os.path.join(root, file)) for file in files]))

    return ans
