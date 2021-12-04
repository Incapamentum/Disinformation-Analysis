"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: initialize_processing.py

    Handles the initialization of processing the
    network files found in the Data subdirectory

    Depending on the option that is passed, will
    either generate a list of random ego nodes
    that will then be used for processing in
    creating a network that is then saved as a
    .txt file
"""


import os
import paths
import sys

from network_processing import collect_ids, random_select, create_network
from scripts.utility import read_file, write_file
from scripts.utility import PROC_USAGE

if (len(sys.argv) != 2):
    print("ERROR!")
    print(PROC_USAGE)
    sys.exit(-1)

# Creating output directory if one doesn't already exist
if (not os.path.isdir(paths.OUTPUT_PATH)):
    os.makedirs(paths.OUTPUT_PATH)

# Creating the specific output directory this script uses
if (not os.path.isdir(paths.EGO_PATH)):
    os.makedirs(paths.EGO_PATH)

arg = sys.argv[1]
node_path = paths.OUTPUT_PATH + "\\selected_nodes.txt"

# Generate list of random ego nodes for processing
if (arg == "-generate"):

    id_path = collect_ids()
    node_list = random_select(id_path)
    write_file(node_list, node_path)

# Process the input graphs
elif (arg == "-process"):

    data = read_file(node_path)
    graph_path = paths.EGO_PATH

    for d in data:

        graph_file = graph_path + f'\\{d}_ego.txt'

        net = create_network(d)
        net.SaveEdgeList(graph_file, f'Ego Network for ego node {d}')

# No valid command was passed
else:

    print("Invalid command!")
    sys.exit(-1)