#!/usr/bin/python3
 """
    Read the contents of a text file and print it to stdout.

    Args:
    - filename (str): The path to the file to be read. Defaults to an empty string.

    Returns:
    - None
    """
def read_file(filename=""):
    with open("my_file_0.txt", mode="r", encoding="utf-8") as file:
            print(file.read(), end ="")
