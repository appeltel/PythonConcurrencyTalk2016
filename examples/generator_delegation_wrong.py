"""
Example of naive delegation to a subgenerator which
does not work correctly with send()
"""


def countdown(counter):
    """
    This countdown generator can be reset/changed by sending
    a new integer.
    """
    while counter > 0:
        new_value = yield counter
        if new_value is not None:
            counter = new_value
        counter = counter - 1

    for item in footrace():
        yield item

def footrace():
    """
    The footrace generator will start over if it is sent
    a string 'fault'
    """
    started = False
    while not started:
        status = yield 'On your marks.'
        if status == 'fault':
            continue
        status = yield 'Set.'
        if status == 'fault':
            continue
        yield 'Go!'
        started = True
