import locale
import socket
import subprocess


def only_work_on(hostname: str):
    """
    a helper function for dev to run code on certain computers
    """
    cur_hostname = socket.gethostname()
    # exit or raise Exception ?
    if hostname != cur_hostname:
        raise Exception(f'expected host: {hostname}; real host: {cur_hostname}')


def run(cmd: str) -> subprocess.CompletedProcess:
    """
    a help wrapper function that you can run a command with cmd without worrying about wrong encoding.
    """
    return subprocess.run(cmd, encoding=locale.getpreferredencoding(), capture_output=True, shell=True)


def exec(cmd: str) -> subprocess.Popen:
    """
    如何获取输出？
    1. 同步获取：程序会在调用 communicate() 时阻塞，不如用 run(cmd)
    outs, errs = exec('java').communicate()
    print(errs.decode(locale.getpreferredencoding()))

    2. 实时读取，要手动处理流对象
    proc = exec('java')
    while True:
        line = proc.stderr.readline()
        # EOF
        if not line:
            break
        print(line.decode(locale.getpreferredencoding()))
    """
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
