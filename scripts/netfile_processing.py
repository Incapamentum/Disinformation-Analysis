"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: collect_node_ids.py

    Used in collecting unique node IDs found in the
    Data/gplus_networks directory
"""

import definitions

from os import listdir
from os.path import isfile, join


def collect_ids():
    """
        Collects all node IDs found in the data path,
        writing it to an output file containing them
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