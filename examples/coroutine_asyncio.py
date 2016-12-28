"""
Example of basic coroutine (PEP492) syntax
to be used by running a simple coroutine
with the asyncio event loop.
"""
import asyncio


async def example(name):
    print('{}: Starting coroutine.'.format(name))
    await asyncio.sleep(0)
    print('{}: Resuming coroutine after first await'.format(name))
    await asyncio.sleep(5)
    print('{}: Resuming coroutine after 5 second sleep'.format(name))
