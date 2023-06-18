def write_file(path, content):
    with open(path, "w") as file:
        file.write(content)


def write_bin(path, content):
    with open(path, "wb") as file:
        file.write(content)


def read_file(path):
    with open(path, "r") as file:
        return file.read()


def append_file(path, content):
    with open(path, "a") as file:
        file.write(content)


def create_file(path):
    try:
        with open(path, "x"):
            pass
    except FileExistsError:
        pass


def read_lines_file(path):
    return read_file(path).splitlines()
