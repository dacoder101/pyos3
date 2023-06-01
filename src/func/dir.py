import os


def create_dir(path):
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        raise OSError(f"Failed to create directory at {path}: {e}")


def remove_dir(path):
    try:
        os.removedirs(path)
    except OSError as e:
        raise OSError(f"Failed to remove directory at {path}: {e}")
