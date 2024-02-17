from tfana.main import list_rc_files


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
