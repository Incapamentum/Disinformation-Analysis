"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: initialize_processing.py

    Handles the initialization of processing the
    network files found in the Data subdirectory
"""


import definitions
import os
import snap
import sys

from network_processing import collect_ids, random_select, create_network
from scripts.utility import read_file, write_file
from scripts.utility import PROC_USAGE

if (len(sys.argv) != 2):
    print("ERROR!")
    print(PROC_USAGE)
    sys.exit(-1)

# Creating output folder if one doesn't already exist
if (not os.path.isdir(definitions.OUTPUT_PATH)):
    os.makedirs(definitions.OUTPUT_PATH)

arg = sys.argv[1]
node_path = definitions.OUTPUT_PATH + "\\" + "selected_nodes.txt"

# Generate list of random ego nodes for processing
if (arg == "-egenrate"):

    id_path = collect_ids()
    node_list = random_select(id_path)
    write_file(node_list, node_path)

elif (arg == "-process"):

    data = read_file(node_path)

    net = create_network(data[0])
