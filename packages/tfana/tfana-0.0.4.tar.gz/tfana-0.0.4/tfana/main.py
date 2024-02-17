import glob
import os


def greet(name):
    return f"Hello, {name}!"


def list_rc_files():
    # 获取用户主目录
    home_directory = os.path.expanduser("~")

    # 使用 glob 模块列出匹配的文件
    rc_files = [
        file
        for file in os.listdir(home_directory)
        if all((os.path.isfile(os.path.join(home_directory, file)), "rc" in file))
    ]

    return rc_files


if __name__ == "__main__":
    print(list_rc_files())
