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
        Updates a value by adding loss

        :param source: Value determines the type of value update to perform
        :param receiver: Value to be updated
        :return:
    """

    # No disinformation spread possible
    if (source >= 0.5):
        return receiver

    # Denotes possible spread of disinformation
    if (source <= -0.5):

        # Denotes a vulnerable value
        if ((receiver > -0.5) and (receiver <= 0.5)):
            return receiver + MAX_LOSS

        # Denotes value approaching saturation
        if (receiver <= -0.5):

            # Saturation has been reached
            if ((receiver + MAX_LOSS) < -1):
                return -1

            return receiver + MAX_LOSS

    # Default return
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
