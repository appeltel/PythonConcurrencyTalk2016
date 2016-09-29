"""
Simple flask application for the See 'n Say (TM) inspired
animals API
"""
from time import sleep

from flask import Flask
app = Flask(__name__)

FARM = {
    'cow': 'Moo!',
    'pig': 'Oink!',
    'sheep': 'Baaa!',
    'chicken': 'Cluck!',
    'bird': 'Tweet!',
    'duck': 'Quack!',
    'dog': 'Woof!',
    'cat': 'Meow!',
    'frog': 'Ribbit!',
    'horse': 'Neigh!',
    'turkey': 'Gobble-Gobble!',
    'rooster': 'Cock-a-Doodle-Doo!'
}


@app.route('/animals/')
def hello():
    """
    Welcome
    """
    msg = 'Welcome to the farm!'
    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}


@app.route('/animals/<animal>')
def speak(animal):
    """
    What does this animal say???
    """
    if animal not in FARM:
        return 'The animal {0} was not found.'.format(animal), 404

    sleep(5)
    return FARM[animal], 200, {'Content-Type': 'text/plain; charset=utf-8'}
