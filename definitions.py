"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: definitions.py

    Contains some global definitions used
    by multiple files throughout the project
"""

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Paths related to data for processing
DATA_PATH = ROOT_PATH + "\\Data"
GPLUS_DATA = DATA_PATH + "\\gplus_networks"

# Paths related to output
OUTPUT_PATH = ROOT_PATH + "\\output"
HUB_PATH = OUTPUT_PATH + "\\hubs"
EGO_PATH = OUTPUT_PATH + "\\ego_nets"
PLOTS_PATH = OUTPUT_PATH + "\\plots"
