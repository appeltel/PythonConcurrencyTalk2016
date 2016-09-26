"""
Example of delegation to a subgenerator using
"yield from" syntax introduced in PEP380 (2009)
and incorporating a return statement
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

    fault_count = yield from footrace()

    yield 'Race started after {0} faults.'.format(fault_count)


def footrace():
    """
    The footrace generator will start over if it is sent
    a string 'fault'. Keeps track of faults and reutrns the
    total.
    """
    started = False
    faults = 0
    while not started:
        status = yield 'On your marks.'
        if status == 'fault':
            faults = faults + 1
            continue
        status = yield 'Set.'
        if status == 'fault':
            faults = faults + 1
            continue
        yield 'Go!'
        started = True

    return faults
