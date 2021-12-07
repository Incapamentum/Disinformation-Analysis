"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: plot_disinformation_coefficient.py

    Plots the resulting averages of the disinformation coefficients
"""

import os
import paths

import matplotlib.pyplot as plt

from scripts.utility import read_json
from simulation.parameters import MAX_CYCLES

# Creating output folder if one doesn't already exist
if (not os.path.isdir(paths.OUTPUT_PATH)):
    os.makedirs(paths.OUTPUT_PATH)

data_path = paths.RESULT_PATH + "\\sim_results.json"
plot_path = paths.PLOTS_PATH + "\\disinformation"
image_name = plot_path + f'\\disinformation_rate.png'

if (not os.path.isdir(plot_path)):
    os.makedirs(plot_path)

data = read_json(data_path)
time_ticks = [x for x in range(MAX_CYCLES + 1)]

for net in data.keys():

    if (net == "104905626100400792399"):
        continue

    disinformation_coeff = data[net]["d_c"]
    plt.scatter(time_ticks, disinformation_coeff, label=net, s=1)

plt.title("Disinformation Across EgoNets")
plt.xlabel("Time ticks")
plt.ylabel("Disinformation Average")
plt.legend(markerscale=5.0)
plt.savefig(image_name)
