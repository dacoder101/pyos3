from func.file import create_file
from func.path import path_exists
from func.util import file_exec
from func.dir import create_dir

BLANKS_PATH = "store/blanks/"


def install():
    if not path_exists(BLANKS_PATH):
        create_dir(BLANKS_PATH)
        create_file(BLANKS_PATH)
        file_exec("install.py")


install()