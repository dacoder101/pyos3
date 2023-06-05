from os import system


def key():
    system("/bin/bash -c 'read -s -n 1 -p \"Press Any Key...\"'")


def cls():
    print("\033c", end="", flush=True)
