from os import system
import termios
import tty
import sys


def get_key():
    fd = sys.stdin.fileno()
    settings = termios.tcgetattr(fd)

    try:
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, settings)

    return key


def key(msg="Press Any Key..."):
    system(f"/bin/bash -c 'read -s -n 1 -p \"{msg}\"'")


def cls():
    print("\033c", end="", flush=True)


def tprint(str):
    TITLE = """
█▀▀█ █──█ █▀▀█ █▀▀ █▀▀█ 
█──█ █▄▄█ █──█ ▀▀█ ──▀▄ 
█▀▀▀ ▄▄▄█ ▀▀▀▀ ▀▀▀ █▄▄█

"""
    print(TITLE + str)
