import os


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


def main():
    rc_files = list_rc_files()

    if rc_files:
        print("Found the following rc files:")
        for rc_file in rc_files:
            print(rc_file)
    else:
        print("No rc files found.")


if __name__ == "__main__":
    main()
