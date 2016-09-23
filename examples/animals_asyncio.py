"""
This module is an asynchronous version of
animals.py in which coroutines
and the asyncio event loop are used
"""
import asyncio

import aiohttp

from radprint import radprint


async def speak(animal, session):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = await session.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = await response.text()
    radprint('The {0} says "{1}".'.format(animal, sound))


async def main():
    """
    Retrieve and print sounds for all animals.
    """
    animals = ['cow', 'pig', 'chicken']
    tasks = []
    with aiohttp.ClientSession() as session:
        for animal in animals:
            fut = asyncio.ensure_future(speak(animal, session))
            tasks.append(fut)

        await asyncio.wait(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
