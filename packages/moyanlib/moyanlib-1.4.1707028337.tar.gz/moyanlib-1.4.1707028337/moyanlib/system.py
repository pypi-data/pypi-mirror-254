import os
import moyanlib.Error as Error


def listdir(path):
    # 列出所有dir
    try:
        object = os.listdir(path)
    except:
        raise Error.file_PathError(path)
    else:
        return object


def remove_file(path):
    # 删除文件
    if os.path.exists(path):
        os.remove(path)


def move_file(src, dst):
    # 重命名
    if os.path.exists(src):
        os.rename(src, dst)


def system(command):
    # 获取system
    object = os.popen(command)
    text = object.read()
    return text
