"""
Module with util functions for testing.
"""


def open_file(file_name: str) -> str:
    """
    Opens file a file and cast its contents to a string.

    Args:
        file_name (str): OS path of the file.

    Returns:
        str: the contents of the file a string.
    """
    with open(file_name, "r") as file:
        file_str = file.read()

    return file_str
