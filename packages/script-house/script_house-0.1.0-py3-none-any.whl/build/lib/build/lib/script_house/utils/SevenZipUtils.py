from . import SystemUtils
from .FileSystemUtils import assert_is_file


class SevenZipUtils:
    __7zPath__ = '7z'

    def __init__(self, path: str = None):
        if path is not None:
            self.__7zPath__ = path
        assert_is_file(self.__7zPath__)

    def extract(self, archive: str, output_dir: str = None):
        assert_is_file(archive)
        cmd = f'{self.__7zPath__} e "{archive}" '
        if output_dir is not None:
            cmd += f'o{output_dir}'
        print(cmd)
        SystemUtils.run(cmd)
