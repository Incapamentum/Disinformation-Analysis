"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: utility.py

    Contains some useful utility functions
"""

PROC_USAGE = "Insufficient arguments!\n\n" \
             "Format: python3 initialize_processing.py [arg]\n" \
             "\targ - can be one of the following:\n" \
             "\t\t-generate: will generate a list of random ego nodes for processing" \
             "\t\t-process: something else"


def read_file(input_path):
    """
        Reads contents of a file, storing data in a list

        :param input_path: Path to read file from
        :return data: Contains the ego node data
    """

    nodes = []

    with open(input_path, "r") as f:
        for line in f:
            data = line.split()
            nodes.append(data[0])

    return nodes


def write_file(item, output_path):
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
