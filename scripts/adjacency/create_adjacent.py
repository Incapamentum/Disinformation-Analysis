"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: create_adjacency.py

    Processes a graph file to create an adjacent
    matrix representative of the network
"""

import os
import paths

from adjacency_helper import list_to_file
from scripts.utility import read_file

# Creating output folder if one doesn't already exist
if (not os.path.isdir(paths.OUTPUT_PATH)):
    os.makedirs(paths.OUTPUT_PATH)

# graph_path = definitions.EGO_PATH

# Creating matrix folder if one doesn't already exist
if (not os.path.isdir(paths.MATRIX_PATH)):
    os.makedirs(paths.MATRIX_PATH)

# Setting up in creating adjacency matrix
data = read_file(paths.NODE_FILE)

for d in data:

    net_file = paths.EGO_PATH + f'\\{d}_ego.txt'
    adjacency_file = paths.MATRIX_PATH + f'\\{d}_adjacency.txt'

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
