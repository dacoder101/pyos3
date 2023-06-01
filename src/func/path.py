import os


def path_exists(path):
    return os.path.exists(path)


def is_file(path):
    return os.path.isfile(path)


def is_dir(path):
    return os.path.isdir(path)
