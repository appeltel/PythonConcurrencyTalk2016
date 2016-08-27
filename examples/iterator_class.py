"""
Example of a simple class implementing iterator
protocol
"""


class Countdown():

    def __init__(self, start):
        self.counter = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 1:
            raise StopIteration
        self.counter -= 1
        return self.counter + 1
