import requests

from radprint import radprint


ANIMALS = ['cow', 'pig', 'chicken']


def process_animal(animal, results):
    """
    Retrieves the sound for the given animal,
    prints it with animation, and then appends
    the sound to the results list.
    """
    response = requests.get(
        'https://ericappelt.com/animals/{0}'.format(animal)
    )
    sound = response.text
    radprint('The {0} says "{1}".'.format(animal, sound))
    results.append(sound)


def main():
    """
    Process all animals and then print a sorted list of
    their sounds.
    """
    results = []
    for animal in ANIMALS:
        process_animal(animal, results)
    results.sort()
    print('\nAnimal sounds: {0}'.format(results))


if __name__ == '__main__':
    main()
