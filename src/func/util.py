from func.file import read_file


def file_exec(path):
    exec(read_file(path), {})
