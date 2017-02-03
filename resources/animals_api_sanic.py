from sanic import Sanic
from sanic.response import text

from asyncio import sleep

app = Sanic(__name__)

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
async def hello(request):
    """
    Welcome
    """
    msg = 'Welcome to the farm!'
    return text(msg, status=200)

@app.route('/animals/<animal>')
async def speak(request, animal):
    """
    What does this animal say???
    """
    if animal not in FARM:
        return text('The animal {0} was not found.'.format(animal), status=404)

    await sleep(5)
    return text(FARM[animal], status=200)
