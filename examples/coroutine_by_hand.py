"""
Example of basic coroutine (PEP492) syntax
to be used by running a simple coroutine
by hand without an actual event loop.
"""
import types


@types.coroutine
def sleep(seconds):
    """
    Basic generator coroutine which another
    coroutine can await on to yield to the
    event loop for a specified time.
    """
    print('sleep: Please wait {0} seconds before resuming.'.format(seconds))
    yield seconds


async def example(name):
    print('{}: Starting coroutine.'.format(name))
    await sleep(0)
    print('{}: Resuming coroutine after first await'.format(name))
    await sleep(5)
    print('{}: Resuming coroutine after 5 second sleep'.format(name))
