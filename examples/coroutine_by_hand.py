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


async def example():
    print('example: Starting example coroutine.')
    await sleep(0)
    print('example: Resuming example coroutine after first await')
    await sleep(5)
    print('example: Resuming example coroutine after 5 second sleep')
