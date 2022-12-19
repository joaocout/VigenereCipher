def read_file(file_path: str) -> list[str]:
    f = open(file_path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines


def main():
    text = read_file("desafio1.txt", "r")
    print(text)


if __name__ == "__main__":
    main()
