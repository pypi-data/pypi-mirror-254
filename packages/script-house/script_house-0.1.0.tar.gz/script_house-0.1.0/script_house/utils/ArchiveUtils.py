import subprocess

from . import SystemUtils
from .FileSystemUtils import assert_is_file, assert_is_path


class BaseArchiveUtils:
    _exe = None

    def __init__(self, path: str = None):
        if path is not None:
            self._exe = path
        assert_is_file(self._exe)


class SevenZipUtils(BaseArchiveUtils):
    def __init__(self, path: str = None):
        super().__init__(path)

    def extract(self, archive: str, output_dir: str = None) -> subprocess.CompletedProcess:
        assert_is_file(archive)
        cmd = f'{self._exe} x "{archive}" '
        if output_dir is not None:
            cmd += f'-o"{output_dir}"'
        return SystemUtils.run(cmd)


class RARUtils(BaseArchiveUtils):
    def __init__(self, path: str = None):
        super().__init__(path)

    def extract(self, archive: str, output_dir: str = None) -> subprocess.CompletedProcess:
        assert_is_file(archive)
        cmd = f'{self._exe} x "{archive}" '
        if output_dir is not None:
            output_dir = output_dir.strip()
            # 必须使用附加的倒斜线来表示目标文件夹
            if output_dir[-1] != '\\':
                output_dir += '\\'
            cmd += f' "{output_dir}"'
        return SystemUtils.run(cmd)

    def add(self,
            output_path: str,
            files: list[str],
            pwd: str = '',
            compress_rate: int = 3,
            recovery_rate: int = None,
            solid_archive: bool = False,
            dict_size: str = '32') -> subprocess.CompletedProcess:

        if '"' in output_path:
            raise Exception('no " in output_path')

        files_str = ""
        for f in files:
            f = f.strip()
            assert_is_path(f)
            files_str += f' "{f}" '

        pwd = pwd.strip()
        if pwd != '':
            if len(pwd) > 126:
                raise Exception("len(pwd) <= 126")
            if '"' in pwd:
                raise Exception('no " in pwd')
            # -hp 加密文件和文件名
            pwd = '-hp"' + pwd + '"'

        if not (0 <= compress_rate <= 5):
            raise Exception('compress_rate should between 0 and 5')

        if recovery_rate:
            if not (1 <= recovery_rate):
                raise Exception('recovery_rate should be greater than 0')
            recovery_rate = '-rr' + str(recovery_rate) + '%'
        else:
            recovery_rate = ''

        # 固实压缩
        if solid_archive:
            solid_archive = '-s'
        else:
            solid_archive = ''

        # 字典大小
        dict_size = '-md' + dict_size

        # -o- 跳过已存在文件。如果已经存在 output_path，则程序返回码是 10
        # -ep1 保留压缩文件夹路径
        # -r0 递归文件夹，但是指定文件时不会递归文件所在的目录
        cmd = f'{self._exe} a {solid_archive} {dict_size}  -ep1 -o- -m{compress_rate} {pwd} {recovery_rate} -r0 "{output_path}" {files_str}'
        return SystemUtils.run(cmd)
