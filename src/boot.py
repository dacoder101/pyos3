from func.path import path_exists
from func.util import file_exec
from func.dir import create_dir
from func.io import cls

BLANKS_PATH = "store/blanks/"


def install():
    if not path_exists(BLANKS_PATH):
        create_dir(BLANKS_PATH)
    if not path_exists(BLANKS_PATH + "installed") and not path_exists(
        BLANKS_PATH + "afterinstall"
    ):
        file_exec("install.py")
    if path_exists(BLANKS_PATH + "afterinstall"):
        file_exec("afterinstall.py")


def main():
    cls()
    install()


if __name__ == "__main__":
    install()
