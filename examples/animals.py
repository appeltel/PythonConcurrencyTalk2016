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
    for animal in animals:
        speak(animal, session)

    session.close()

if __name__ == '__main__':
    main()
