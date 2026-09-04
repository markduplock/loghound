import sys


def read_file(filename: str) -> str:
    with open(filename, "r") as file:
        content = file.read()

    return content


def get_args() -> str:
    f: str = sys.argv[1]
    return f


def main() -> None:
    filename: str = get_args()
    print(read_file(filename))


if __name__ == "__main__":
    main()
