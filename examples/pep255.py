"""
Example of a simple generator function
"""


def countdown(counter):
    while counter > 0:
        yield counter
        counter -= 1
