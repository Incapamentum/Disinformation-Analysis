"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: create_adjacency.py

    Processes a graph file to create an adjacent
    matrix representative of the network
"""

import definitions
import os

from adjacency_helper import list_to_file
from scripts.utility import read_file

# Creating output folder if one doesn't already exist
if (not os.path.isdir(definitions.OUTPUT_PATH)):
    os.makedirs(definitions.OUTPUT_PATH)

# matrix_path = definitions.OUTPUT_PATH + "\\matrix"
graph_path = definitions.EGO_PATH
node_path = definitions.OUTPUT_PATH + "\\selected_nodes.txt"

# Creating matrix folder if one doesn't already exist
if (not os.path.isdir(definitions.MATRIX_PATH)):
    os.makedirs(definitions.MATRIX_PATH)

# Setting up in creating adjacency matrix
data = read_file(node_path)

for d in data:

    net_file = graph_path + f'\\{d}_ego.txt'
    adjacency_file = definitions.MATRIX_PATH + f'\\{d}_adjacency.txt'

    with open(net_file, "r") as f:

        # Skipping lines of no interest
        for t in range(2):
            next(f)

        line = f.readline()
        nodes = int(line.split()[2])

        # Creating an adjacency matrix of fixed size
        adjacency = [[0 for x in range(nodes)] for y in range(nodes)]

        # Skipping next line
        next(f)

        # Adding directed edges to the matrix
        for line in f:

            edge = line.split()
            s = int(edge[0])
            e = int(edge[1])

            adjacency[s][e] = 1

    list_to_file(adjacency, adjacency_file)
