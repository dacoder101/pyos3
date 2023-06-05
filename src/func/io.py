from os import system


def key(msg="Press Any Key..."):
    system(f"/bin/bash -c 'read -s -n 1 -p \"{msg}\"'")


def cls():
    print("\033c", end="", flush=True)
