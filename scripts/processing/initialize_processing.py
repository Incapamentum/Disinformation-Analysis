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

from network_processing import collect_ids, random_select
from scripts.utility import write_output

# Creating output folder if one doesn't already exist
if (not os.path.isdir(definitions.OUTPUT_PATH)):
    os.makedirs(definitions.OUTPUT_PATH)

id_path = collect_ids()
node_list = random_select(id_path)

node_path = definitions.OUTPUT_PATH + "\\" + "selected_nodes.txt"

write_output(node_list, node_path)
