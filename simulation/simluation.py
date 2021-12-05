"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: simulation.py

    Comments
"""

import sim_helper as sh
import parameters as params
import paths as p

import os
import sys

from copy import deepcopy
from datetime import timedelta
from math import floor
from math import log2
from scripts.utility import read_file
from timing import Timer

# Creating output folder if one doesn't already exist
if (not os.path.isdir(p.OUTPUT_PATH)):
    os.makedirs(p.OUTPUT_PATH)

# Creating results folder if one doesn't already exist
if (not os.path.isdir(p.RESULT_PATH)):
    os.makedirs(p.RESULT_PATH)

# Checking to make sure directory exists
if (not os.path.isdir(p.MATRIX_PATH)):
    msg = "Directory does not exist!\n\n"
    msg += f'The directory {p.MATRIX_PATH} does not exist!\n'
    sh.error(msg)
    sys.exit(-1)

hub_file = p.HUB_PATH + "\\ego_hubs.json"
results_file = p.RESULT_PATH + "\\sim_results.json"

data = read_file(p.NODE_FILE)
hub_nodes = sh.read_json(hub_file)

results = {}

# Measuring execution of whole simulation
timer = Timer()
timer.start_time()

for d in data:

    # Setting up variables for each egonet
    hubs = hub_nodes[d]

    results[d] = []
    adj_file = p.MATRIX_PATH + f'\\{d}_adjacency.txt'

    adjacency = sh.populate_adjacency(adj_file)
    num_nodes = len(adjacency)
    depth = floor(log2(num_nodes))

    # Represents how susceptible each node is to disinformation
    disinformation_coefficient = sh.uniform_populate(num_nodes)

    # Adjusting the disinformation coefficients to the hub nodes which are
    # specific propagators of disinformation
    for h in hubs:
        disinformation_coefficient[h] = -1

    # Saving disinformation coefficient average at time tick 0
    results[d].append(sh.average(disinformation_coefficient))

    # Disconnecting ego node from the rest of the hubs
    for h in hubs:
        if (h == 0):
            continue
        adjacency[0][h] = 0

    # Initial list of active nodes are hub nodes
    active = deepcopy(hubs)

    # Beginning post cycle
    for i in range(params.MAX_CYCLES):

        for node in active:

            # Randomly selecting outgoing edges to spread post
            # contact
            contact = 0

            while ((sh.outgoing_check(adjacency[node])) and (contact < params.MAX_CONTACT)):

                index = sh.random_index(adjacency[node])
                source_val = disinformation_coefficient[node]
                receive_val = disinformation_coefficient[index]
                disinformation_coefficient[index] = sh.update_value(source_val, receive_val)

                contact += 1

        sh.add_propagators(active, disinformation_coefficient)

        # Record new disinformation average of network
        results[d].append(sh.average(disinformation_coefficient))

timer.end_time()
timer.elapsed_time()

total_time = str(timedelta(seconds=timer.elapsed))

print(f'Total execution time: {total_time}')

# Write the results to a JSON file
sh.write_json(results, results_file)
