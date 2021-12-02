"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: network_processing.py

    Contains functions used in the processing of files
    associated with network files found in the
    Data directory
"""

import definitions as d

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

    data_path = d.GPLUS_DATA
    output_file = d.OUTPUT_PATH + "\\" + "node_ids.txt"

    file_list = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    node_ids = []

    for i in range(0, len(file_list)):

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


def create_network(ego_node):
    """
        Constructs the network around the specified ego_node

        :param ego_node: ID of the ego node
        :return:
    """

    # Edges contain node information
    ego_edges = d.GPLUS_DATA + f'\\{ego_node}.edges'

    nodes = []
    edges = []

    # Aggregating all nodes into a single structure
    with open(ego_edges, "r") as f:
        for line in f:
            data = line.split()
            nodes += data

    # Removing dupes in nodes
    nodes = list(set(nodes))

    # Aggregating all edges into a single structure
    with open(ego_edges, "r") as f:
        for line in f:
            data = line.split()
            edges.append(data)

    # Useful mapping to ensure each generated ID can
    # be traced back to its file original
    id_to_node = {}

    # Creating network
    ego_net = snap.TNEANet.New()

    # Adding ego node to network
    id_to_node[ego_node] = ego_net.AddNode(-1)

    # Adding the rest of nodes to network, connecting
    # them to ego node as well
    for n in nodes:
        id_to_node[n] = ego_net.AddNode(-1)
        ego_net.AddEdge(id_to_node[ego_node], id_to_node[n])

    # Connecting all other nodes according to edge file
    for e in edges:
        ego_net.AddEdge(id_to_node[e[0]], id_to_node[e[1]])

    return ego_net
