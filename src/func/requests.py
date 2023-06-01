from requests.exceptions import RequestException
from func import file
import requests


def check_internet(url, attempts=3):
    for _ in range(attempts):
        try:
            requests.get(url)
            return True
        except RequestException:
            pass
    return False


def download(url, path):
    try:
        file.create_file(path)
        file.write_file(path, requests.get(url))
    except RequestException:
        raise f"Failed to download from {url}"
