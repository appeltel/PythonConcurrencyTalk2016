"""
Example of a simple class implementing iterator
protocol (PEP 232)
"""


class Countdown():

    def __init__(self, start):
        self.counter = start + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter = self.counter - 1
        if self.counter < 1:
            raise StopIteration
        return self.counter
