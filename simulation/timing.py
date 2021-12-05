"""
    Author: Gustavo Diaz Galeas
    UCF ID: 3520029
    Course: COP 5537

    File name: timing.py

    Simple TImer object to measure script execution
    times
"""

import time


class Timer:

    def __init__(self):
        self.active = False

        self.elapsed = 0

        self.start = 0
        self.end = 0

    def start_time(self):
        """
            Initializes the start value of the Timer.

            :return: Nothing
        """

        if (not self.active):
            self.start = time.time()
            self.active = True

    def end_time(self):
        """
            Initializes the end value of the Timer

            :return: Nothing
        """

        if (self.active):
            self.end = time.time()
            self.active = False

    def elapsed_time(self):
        """
            Initializes the total elapsed time of the Timer

            :return: Nothing
        """

        if (not self.active):
            self.elapsed = self.end - self.start

    def reset_timer(self):
        """
            Resets all values back to their default

            :return: Nothing
        """

        if (not self.active):
            self.start = 0
            self.end = 0
            self.elapsed = 0
