"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: utility.py

    Contains some useful utility functions
"""

import json

PLOT_USAGE = "Insufficient arguments!\n\n" \
             "Format: python3 plot_deg_distribution.py [arg] [option]\n" \
             "\targ - can be one of the following:\n" \
             "\t\t-dist - denotes the degree distribution\n" \
             "\toption - can be one of the following:\n" \
             "\t\tdeg - obtain the degree distribution of the network\n" \
             "\t\tin - obtain the in-degree distribution of the network\n" \
             "\t\tout - obtain the out-degree distribution of the network\n" \

PROC_USAGE = "Insufficient arguments!\n\n" \
             "Format: python3 initialize_processing.py [arg]\n" \
             "\targ - can be one of the following:\n" \
             "\t\t-generate: will generate a list of random ego nodes for processing\n" \
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


def read_json(file_name):
    """
        Loads the contents written to a
        JSON file

        :param file_name: Name of JSON file
        :return data: JSON data
    """

    with open(file_name, "r") as f:
        data = json.loads(f.read())

    return data


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


def write_json(data, file_name):
    """
        Writes data to JSON

        :param data: Dictionary to write to JSON
        :param file_name: Name of the intended JSON file
        :return: Nothing
    """

    with open(file_name, "w") as f:
        json.dump(data, f)
