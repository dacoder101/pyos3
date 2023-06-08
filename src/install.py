from func.io import tprint, key
from func import requests

INTERNET_URL = "https://github.com/"


def main():
    if not requests.check_internet(INTERNET_URL):
        tprint(
            f"Your internet was not able to connect with the test URL {INTERNET_URL}.\nThe process can not continue without an internet connection."
        )
        key()
        exit()
    tprint("Pyos3 will begin to install.\nThe process may use up to 10MB of data.")
    key()


main()
