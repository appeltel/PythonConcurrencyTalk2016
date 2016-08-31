"""
Human event loop

Simple example of coroutines designed to be executed by
a human using the python REPL.

This version uses regular generator functions as coroutines.
"""
from queue import Queue, Empty
from datetime import datetime, timedelta

class ToDoList(Queue):
    """
    Special Queue to keep track of coroutines for the human event
    loop to run and when to run them. 
    """
    def add(self, coro, delay=0):
        """
        Add a coroutine to the queue with a delay in seconds before it
        should next be run.
        """
        when = datetime.now() + timedelta(seconds=delay)
        self.put((coro, when))

    def remove(self):
        """
        Retrieve the next coroutine from the queue. Tell the human if
        it is ready to run or should be returned with a delay.
        """
        try:
            coro, when = self.get()
            if when < datetime.now():
                print('ToDoList: Run this coroutine now')
            else:
                delay = (when - datetime.now()).seconds
                print(
                    'ToDoList: Put this coro back with delay {0}'
                    .format(delay)
                )
            return coro
        except Empty:
            print('Nothing to do.')


def hel_sleep(n):
    if n == 0:
        yield 'Please call us back as soon as possible'
    else:
        yield 'Please call us back after {0} seconds'.format(n)


def my_coro(name):
    """
    Example coroutine that delegates to hel_sleep
    and prints its name.
    """
    print('{0}: Starting'.format(name))
    yield from hel_sleep(0)
    print('{0}: Doing More Stuff'.format(name))
    yield from hel_sleep(30)
    print('{0}: Finishing Up'.format(name))
    return 'Done!'


def hel_schedule(coro):
    hel_todo.add(coro, delay=0)
    return coro


hel_todo = ToDoList()
