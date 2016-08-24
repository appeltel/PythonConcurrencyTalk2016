from time import sleep
import sys

def radprint(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(0.05)
    sys.stdout.write('\n')
