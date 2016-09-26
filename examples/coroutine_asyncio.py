"""
Example of basic coroutine (PEP492) syntax
to be used by running a simple coroutine
with the asyncio event loop.
"""
import asyncio


async def example():
    print('example: Starting example coroutine.')
    await asyncio.sleep(0)
    print('example: Resuming example coroutine after first await')
    await asyncio.sleep(5)
    print('example: Resuming example coroutine after 5 second sleep')
