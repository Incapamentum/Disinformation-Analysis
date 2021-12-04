"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: hub_collect.py

    Collects all the node hubs for each egonet. Hubs are
    nodes that connect to a vast majority of the network
"""

import json
import os
import paths
import snap

import statistics as stat

from scripts.utility import read_file

graph_path = paths.OUTPUT_PATH + "\\"
hub_file = paths.HUB_PATH + "\\" + "ego_hubs.json"

# Creating output folder if one doesn't already exist
if (not os.path.isdir(paths.OUTPUT_PATH)):
    os.makedirs(paths.OUTPUT_PATH)

# Creating a hub subdirectory within the output path
if (not os.path.isdir(paths.HUB_PATH)):
    os.makedirs(paths.HUB_PATH)

# Testing stuff out
data = read_file(paths.NODE_FILE)

ego_hubs = {}

for d in data:

    ego_file = f'{d}_ego.txt'
    net_file = graph_path + ego_file

    net = snap.LoadEdgeList(snap.TNEANet, net_file, 0, 1, '\t')

    deg_vertex = net.GetDegCnt()

    deg_cnt = []

    for item in deg_vertex:
        deg_cnt.append(item.GetVal1())

    # Calculating some stat results
    st_dev = stat.stdev(deg_cnt)
    mean = stat.mean(deg_cnt)
    q3 = mean + (.675 * st_dev)
    iqr = 1.35 * st_dev
    outlier_cutoff = int(q3 + (1.5 * iqr))

    # Detecting outliers in the data, indicating hubs
    cnt = 0
    new_deg_cnt = deg_cnt[(len(deg_cnt) // 2) : len(deg_cnt)]

    # Collecting all outlying values
    outliers = []

    for c in new_deg_cnt:

        if (c >= outlier_cutoff):
            outliers.append(c)

    # Collecting the nodes that correspond with the above outliers
    hubs = []

    for node in net.Nodes():

        deg = node.GetInDeg() + node.GetOutDeg()

        if (deg in outliers):
            hubs.append(node.GetId())

    ego_hubs[d] = hubs

with open(hub_file, "w") as f:
    json.dump(ego_hubs, f)