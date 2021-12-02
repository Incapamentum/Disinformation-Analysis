"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: adjacency_helper.py


"""


def list_to_file(l, file_name):
    """
        Writes the contents of a list to
        an output file

        :param l: list to be converted to file
        :param file_name: name of the file to write to
        :return: Nothing
    """

    size = len(l)

    with open(file_name, "a") as f:

        for i in range(size):

            line = f'{i}\t'

            for j in range(size):
                if (j == (size - 1)):
                    line += f'{l[i][j]}\n'
                else:
                    line += f'{l[i][j]},'

            f.write(line)
