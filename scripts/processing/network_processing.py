"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: network_processing.py

    Contains functions used in the processing of files
    associated with network files found in the
    Data directory
"""

import definitions
import snap

from os import listdir
from os.path import isfile, join
from random import shuffle


def collect_ids():
    """
        Collects all node IDs found in the data path,
        writing it to a file containing them.

        :return:
            Path of the file containing node IDss
    """

    data_path = definitions.GPLUS_DATA
    output_file = definitions.OUTPUT_PATH + "\\" + "node_ids.txt"

    file_list = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    node_ids = []

    for i in range(0, len(file_list), 2):

        collect = file_list[i].split(sep=".")
        node_ids.append(collect[0])

    with open(output_file, "w") as f:
        f.write("\n".join(node_ids))

    return output_file


def random_select(file_name):
    """
        Given the name (or path) of a file, process it to
        randomly return five egonets

        :param file_name: Name (or path) of the file to process
        :return: a list of ego node IDs
    """

    collect = []
    rand_nodes = []

    with open(file_name, "r") as f:
        for line in f:
            line = line.split()
            collect.append(line[0])

    for i in range(5):
        shuffle(collect)
        rand_nodes.append(collect.pop())

    return rand_nodes
