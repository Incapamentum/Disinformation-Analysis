"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: definitions.py

    Contains various global path variables
"""

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Paths related to data for processing
DATA_PATH = ROOT_PATH + "\\Data"
GPLUS_DATA = DATA_PATH + "\\gplus_networks"

# Main output path
OUTPUT_PATH = ROOT_PATH + "\\output"

# Files within the main output path
NODE_FILE = OUTPUT_PATH + "\\selected_nodes.txt"

# Subdirectory output paths
EGO_PATH = OUTPUT_PATH + "\\ego_nets"
HUB_PATH = OUTPUT_PATH + "\\hubs"
MATRIX_PATH = OUTPUT_PATH + "\\matrix"
PLOTS_PATH = OUTPUT_PATH + "\\plots"
RESULT_PATH = OUTPUT_PATH + "\\results"
