"""
This module is an asynchronous version of
animals.py in which a generator-coroutine
and asyncio event loop are used
"""
import asyncio

import aiohttp

from radprint import radprint


@asyncio.coroutine
def speak(animal):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = yield from aiohttp.request(
        'GET',
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = yield from response.text()
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
