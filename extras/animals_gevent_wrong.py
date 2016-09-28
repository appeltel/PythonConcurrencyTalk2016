"""
This module is a naive gevent version of
animals.py in which the animated printing
is not properly synchronized. This demostrates
the similarity between using implicit coroutines
and threads from the perspective of the
application developer.
"""
from gevent import monkey
monkey.patch_all()

import gevent
import requests

from radprint import radprint


def speak(animal, session):
    """
    Retrieves the sound for the given animal,
    and prints it with animation.
    """
    response = session.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    radprint('The {0} says "{1}".'.format(animal, sound))


def main():
    """
    Retrieve and print sounds for all animals.
    """
    animals = ['cow', 'pig', 'chicken']
    session = requests.Session()
    greenlets = []
    for animal in animals:
        worker = gevent.spawn(speak, animal, session)
        greenlets.append(worker)
        worker.start()

    gevent.joinall(greenlets)
    session.close()


if __name__ == '__main__':
    main()
