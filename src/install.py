from func.io import tprint, key, cls
from func.file import create_file
from func.path import path_exists
from func.util import bad_script
from func import requests

INTERNET_URL = "https://github.com/"
RAW_URL = "https://raw.githubusercontent.com/dacoder101/pyos3/main/"

BLANKS_PATH = "store/blanks/"


def install():
    requests.download(
        f"{RAW_URL}src/afterinstall.py",
        "afterinstall.py",
    )
    create_file(BLANKS_PATH + "afterinstall")
    tprint("Installation has been completed.")
    key()


def main():
    if not requests.check_internet(INTERNET_URL):
        tprint(
            f"Your internet was not able to connect with the test URL {INTERNET_URL}.\nThe process can not continue without an internet connection."
        )
        key()
        exit()
    tprint("Pyos3 will begin to install.\nThe process may use up to 10MB of data.")
    key()
    cls()
    install()


main()
