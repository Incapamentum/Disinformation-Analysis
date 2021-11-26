"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: initialize_analysis.py


"""

import definitions
import os
import snap
import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

from network_analysis import calculate_percent
from scripts.utility import ANAL_USAGE
from scripts.utility import read_file

if (len(sys.argv) != 3):
    print("ERROR!")
    print(ANAL_USAGE)
    sys.exit(-1)

# Creating output folder if one doesn't already exist
if (not os.path.isdir(definitions.OUTPUT_PATH)):
    os.makedirs(definitions.OUTPUT_PATH)

arg = sys.argv[1]
opt = sys.argv[2]

plot_path = definitions.OUTPUT_PATH + "\\" + "plots"
graph_path = definitions.OUTPUT_PATH + "\\"
node_path = definitions.OUTPUT_PATH + "\\" + "selected_nodes.txt"

# Creating image folder if one doesn't already exist
if (not os.path.isdir(plot_path)):
    os.makedirs(plot_path)

# Creating other subdirectories within image folder
deg_path = plot_path + "\\" + "degree"
in_path = plot_path + "\\" + "in_degree"
out_path = plot_path + "\\" + "out_degree"

if (not os.path.isdir(deg_path)):
    os.makedirs(deg_path)

if (not os.path.isdir(in_path)):
    os.makedirs(in_path)

if (not os.path.isdir(out_path)):
    os.makedirs(out_path)

# Generate degree distributions for each ego network
if (arg == "-dist"):

    # Setting up
    data = read_file(node_path)

    for d in data:

        ego_file = f'{d}_ego.txt'
        net_file = graph_path + ego_file

        net = snap.LoadEdgeList(snap.TNEANet, net_file, 0, 1, '\t')
        total_nodes = net.GetNodes()

        if (opt == "deg"):

            image_name = deg_path + "\\" + f'{d}_deg.png'
            title = f'Degree Distribution of {d}'

            deg_vertex = net.GetDegCnt()

            deg_cnt = []
            num_nodes = []

            # Collecting values of all degree counts
            for item in deg_vertex:
                deg_cnt.append(item.GetVal1())
                num_nodes.append(item.GetVal2())

            # Obtaining probabilities of distribution
            p = []

            for n in num_nodes:
                p.append(calculate_percent(n, total_nodes))

        elif (opt == "in"):

            image_name = in_path + "\\" + f'{d}_ideg.png'
            title = f'In-Degree Distribution of {d}'

            in_deg_count = net.GetInDegCnt()

            # Collecting the contents of in-degree count
            deg_cnt = []
            num_nodes = []

            for item in in_deg_count:
                deg_cnt.append(item.GetVal1())
                num_nodes.append(item.GetVal2())

            # Obtaining probabilities of degree distribution
            p = []

            for n in num_nodes:
                p.append(calculate_percent(n, total_nodes))

        elif (opt == "out"):

            image_name = out_path + "\\" + f'{d}_odeg.png'
            title = f'Out-Degree Distribution of {d}'

            out_deg_count = net.GetOutDegCnt()

            # Collecting the contents of out-degree count
            deg_cnt = []
            num_nodes = []

            for item in out_deg_count:
                deg_cnt.append(item.GetVal1())
                num_nodes.append(item.GetVal2())

            # Obtaining probabilities of degree distribution
            p = []

            for n in num_nodes:
                p.append(calculate_percent(n, total_nodes))

        # Setting up density function
        density = np.vstack([deg_cnt, p])
        df = st.gaussian_kde(density)(density)

        # Plotting scatter
        plt.scatter(deg_cnt, p, c=df, s=50)
        plt.title(title)
        plt.xlabel("degree, k")
        plt.ylabel("frequency")
        plt.savefig(image_name)
