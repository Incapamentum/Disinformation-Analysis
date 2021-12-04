"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: plot_deg_distribution.py

    Plots the different degree distributions of each egonet. Three
    types of plots are created: one for in-degree, another for out-degree,
    and a third for total degree
"""

import os
import paths
import snap
import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

from network_analysis import calculate_percent
from scripts.utility import PLOT_USAGE
from scripts.utility import read_file

if (len(sys.argv) != 3):
    print("ERROR!")
    print(PLOT_USAGE)
    sys.exit(-1)

# Creating output folder if one doesn't already exist
if (not os.path.isdir(paths.OUTPUT_PATH)):
    os.makedirs(paths.OUTPUT_PATH)

arg = sys.argv[1]
opt = sys.argv[2]

graph_path = paths.EGO_PATH

# Creating image folder if one doesn't already exist
if (not os.path.isdir(paths.PLOTS_PATH)):
    os.makedirs(paths.PLOTS_PATH)

# Creating other subdirectories within image folder
deg_path = paths.PLOTS_PATH + "\\" + "degree"
in_path = paths.PLOTS_PATH + "\\" + "in_degree"
out_path = paths.PLOTS_PATH + "\\" + "out_degree"

if (not os.path.isdir(deg_path)):
    os.makedirs(deg_path)

if (not os.path.isdir(in_path)):
    os.makedirs(in_path)

if (not os.path.isdir(out_path)):
    os.makedirs(out_path)

# Generate degree distributions for each ego network
if (arg == "-dist"):

    # Setting up
    data = read_file(paths.NODE_FILE)

    for d in data:

        net_file = graph_path + f'\\{d}_ego.txt'

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

            image_name = in_path + "\\" + f'{d}_ideg'
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

        else:
            print("Invalid option!")
            sys.exit(-1)

        # Setting up density function
        density = np.vstack([deg_cnt, p])
        df = st.gaussian_kde(density)(density)

        # Plotting scatter
        plt.scatter(deg_cnt, p, c=df, s=50)
        plt.title(title)
        plt.xlabel("degree, k")
        plt.ylabel("frequency")
        plt.savefig(image_name)
