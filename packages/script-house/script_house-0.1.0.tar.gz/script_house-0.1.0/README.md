# script-house
> *人是喜欢折中的。*
> 
> 如果让我用 Python，我是不愿意的。
> 
> 但如果让我用 DOS 命令写脚本，我一定勤勤恳恳地学 Python。


这个仓库是一个方便日常使用的 python 工具包 —— [`script-house`](https://pypi.org/project/script-house/)。

开箱即用的功能以 `xxOperation` 的形式命名，目前已有：
- [FileSystemOperation.py](script_house%2FFileSystemOperation.py)

但是 [`script_house.utils`](script_house/utils) 包中的功能实际上更为有用



# 如何本地安装

```shell
python.exe .\setup.py bdist_wheel sdist
pip install .
```

# 如何上传到 pypi
1. 拿 `api_token`

2. 创建 .pypirc 文件，放到 `$HOME` 目录（Windows 的话，放到 `C:\Users\用户名` 下）
   .pypirc 格式：

    ```ini
    [pypi]
      username = __token__
      password = <api_token>
    ```

3. `pip install wine`

4. 上传：`twine upload dist/*`



# os-shell-script
以前的脚本，待用 python 重构

## windows-cmd

| 脚本名                   | 作用                                               |
| ------------------------ | -------------------------------------------------- |
| random-open.cmd          | （使用指定软件）打开**当前**文件夹下的一个随机文件 |
| generate-random-file.cmd | 在当前目录下生成一个随机文本文件                   |

## linux-shell

| 脚本名                           | 作用                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------- |
| start-mysql-cluster-in-docker.sh | 启动一个临时的一主二从 MySQL 主从复制集群，<br/>以 3 个 Docker 容器的形式运行 |
| start-redis-cluster-in-docker.sh | 启动一个临时的3主3从的 Redis 集群，<br/> 以 6 个 Docker 容器的形式运行        |
| start-kafka.sh                   | 按照顺序，依次启动 Zookeeper 和 Kafka                                         |
| stop-kafka.sh                    | 按照顺序，依次停止 Kafka 和 Zookeeper                                         |


## powershell
| 脚本名                                | 作用                                                                         |
| ------------------------------------- | ---------------------------------------------------------------------------- |
| random-open.ps1                       | （使用指定软件）打开**当前**文件夹下的一个随机文件                           |
| random-open-from-multiple-folders.ps1 | （使用指定软件）打开**多个**文件夹下的一个随机文件                           |
| extract-markdown-image.ps1            | 解析 markdown 文件中引用的所有本地图片的路径，<br/>并拷贝/剪切到指定文件夹内 |