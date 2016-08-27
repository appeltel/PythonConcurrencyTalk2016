"""
This module is an asynchronous version of
animals.py in which a native coroutine
and asyncio event loop are used
"""
import asyncio

import aiohttp

from radprint import radprint


async def speak(animal):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = await aiohttp.request(
        'GET',
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = await response.text()
    radprint('The {0} says "{1}".'.format(animal, sound))


def main():
    """
    Process all animals and then print a sorted list of
    their sounds.
    """
    animals = ['cow', 'pig', 'chicken']
    tasks = []
    for animal in animals:
        fut = asyncio.ensure_future(speak(animal))
        tasks.append(fut)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))


if __name__ == '__main__':
    main()
