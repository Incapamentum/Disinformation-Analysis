"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: initialize.py

    Handles some initialization of the overall
    project directory structure
"""


import definitions
import os

from netfile_processing import collect_ids

# Creating output folder if one doesn't already exist
if (not os.path.isdir(definitions.OUTPUT_PATH)):
    os.makedirs(definitions.OUTPUT_PATH)

collect_ids()