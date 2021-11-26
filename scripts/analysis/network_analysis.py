"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: network_analysis.py

    Contains helper functions used in the analysis of
    any incoming network
"""


def calculate_percent(num_nodes, total_nodes):
    """
        Calculates the percent given a fixed
        number of nodes from the total amount
        of nodes

        :param num_nodes: number of nodes
        :param total_nodes: total number of nodes
        :return: the percent as a float, rounded up to 6 decimals
    """

    r = num_nodes / total_nodes

    return round(r, 6)
