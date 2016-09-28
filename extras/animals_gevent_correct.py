"""
This module is a naive gevent version of
animals.py in which the animated printing
is properly synchronized with a semaphore.
"""
from gevent import monkey
monkey.patch_all()

import gevent
from gevent.lock import Semaphore
import requests

from radprint import radprint


def speak(animal, session, printlock):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = session.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    with printlock:
        radprint('The {0} says "{1}".'.format(animal, sound))


def main():
    """
    Retrieve and print sounds for all animals.
    """
    animals = ['cow', 'pig', 'chicken']
    session = requests.Session()
    printlock = Semaphore()
    greenlets = []
    for animal in animals:
        worker = gevent.spawn(speak, animal, session, printlock)
        greenlets.append(worker)
        worker.start()

    gevent.joinall(greenlets)
    session.close()


if __name__ == '__main__':
    main()
