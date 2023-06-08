from func.file import create_file
from func.path import path_exists
from func.util import file_exec
from func.dir import create_dir

BLANKS_PATH = "store/blanks/"


def install():
    if not path_exists(BLANKS_PATH):
        create_dir(BLANKS_PATH)
    if not path_exists(BLANKS_PATH + "installed"):
        create_file(BLANKS_PATH + "install")
        file_exec("install.py")

if __name__ == "__main__":
    install()