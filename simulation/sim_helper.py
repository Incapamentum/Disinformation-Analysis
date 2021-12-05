"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: sim_helper.py

    Contains helper functions used in the
    running of the simulator
"""

import json

from parameters import MAX_LOSS
from random import choice
from random import uniform


def add_propagators(active_prop, d_c):
    """
        Adds propagators to the list of active ones
        for further propagation of disinformation

        :param active_prop: List of active propagators
        :param d_c: The list of disinformation coefficients associated with every node
        :return: Nothing
    """

    for i in range(len(d_c)):
        if ((d_c[i] <= -0.5) and (i not in active_prop)):
            active_prop.append(i)


def average(lst):
    """
        Finds the average value of
        a list

        :param lst: List of ints
        :return: The average value of the list
    """

    return sum(lst) / len(lst)


def error(msg):
    """
        Prints an error message

        :param msg: the error message
        :return: Nothing
    """

    print("ERROR: " + msg)


def list_string_to_int(l_str):
    """
        Converts a list of strings to
        a list of integers

        :param l_str: a 2D list of strings
        :return l_int: a 1D list of ints
    """

    l_int = []

    for i in range(len(l_str)):
        l_int.append(int(l_str[i]))

    return l_int


def outgoing_check(row):
    """
        Does a check to see if a node has
        any outgoing edges

        :param row: Node to check
        :return: True if there are outgoing edges, False otherwise
    """

    if (1 in row):
        return True

    return False


def populate_adjacency(file_name):
    """
        Creates an adjacency matrix based on the
        input file

        :param file_name: Name of the network to read from
        :return adjacency: a 2D list representing the network
    """

    adjacency = []

    with open(file_name, "r") as f:
        for line in f:
            data = line.split()
            weights = data[1].split(",")

            weights = list_string_to_int(weights)
            adjacency.append(weights)

    return adjacency


def random_index(lst):

    index = []

    for i in range(len(lst)):
        if (lst[i] == 1):
            index.append(i)

    return choice(index)


def read_json(file_name):
    """
        Loads the contents written to a
        JSON file

        :param file_name: Name of JSON file
        :return data: JSON data
    """

    with open(file_name, "r") as f:
        data = json.loads(f.read())

    return data


def update_value(source, receiver):
    """

        :param source: Value determines the type of value update to perform
        :param receiver: Value to be updated
        :return:
    """

    if (source >= 0.5):
        return receiver

    # Denotes a vulnerable value
    if ((receiver > -0.5) and (receiver <= 0.5)):

        # Check to see if source will cause receiver to become more
        # disinformed
        if (source <= -0.5):
            return receiver + MAX_LOSS

    return receiver


def uniform_populate(size):
    """
        Creates an array filled with values that are a part
        of a uniform distribution

        :param size: Size of the distribution array
        :return distribution: Array containing the uniform distribution
    """

    distribution = []

    for i in range(size):
        distribution.append(uniform(-1, 1))

    return distribution


def write_json(data, file_name):

    with open(file_name, "w") as f:
        json.dump(data, f)
