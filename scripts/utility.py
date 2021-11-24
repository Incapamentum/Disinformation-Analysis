"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: utility.py

    Contains some useful utility functions
"""


def write_output(item, output_path):
    """
        Given an item, writes contents of it
        to a file specified by output_path

        :param item: The item to write contents of to file
        :param output_path: Path to write file to
        :return: Nothing
    """

    if (isinstance(item, list)):
        n = len(item)

        data = ""

        for i in range(n):
            data += f'{item[i]}\n'

        with open(output_path, "w") as f:
            f.write(data)
