#!/usr/bin/python3
"""Read the contents of a text file and print it to stdout."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open("my_file_0.txt", mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
