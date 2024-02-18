import os
from FileSystemUtils import assert_is_file

__7zPath__ = "7z"


def set_7z_path(path: str):
    if not os.path.isfile(path):
        raise Exception(f'not a valid path:{path}')
    __7zPath__ = path


def extract(archive: str, output_dir: str = None):
    assert_is_file(archive)
    cmd = f'{__7zPath__} e "{archive}" '
    if output_dir is not None:
        cmd += f'o{output_dir}'
    os.system(cmd)
