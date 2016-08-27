# PythonConcurrencyTalk2016

Examples, resources, and outline for the python concurrency
and coroutines talk 2016.

### Title

A brief introduction to concurrency and coroutines in Python 3.5

### Synopsis

This is a beginner-friendly introduction to concurrent programming
in Python 3.5. Using a simple example task, differences in threaded
and cooperative approaches to concurrency will be illustrated.
The talk will then focus on how coroutines have developed in
Python from iteration protocol and generators to the new
async/await syntax, and how coroutines
can be used with the provisional "asyncio" event loop in the Python
standard library. It will be assumed that the listener has a basic
understanding of functions, classes, and exceptions in Python, but
no prior knowledge of concurrent programming is required.

### Outline

- Begin with example task of retrieving animal noises from the slow
  animals API and printing them using animation. Discuss difference
  between parallelism and concurrency, need for the latter in this
  situation.

- Show threaded example of animals module, demonstrate need for
  a simple Lock when performing the animation. Discuss preemptive
  and cooperative approaches, desire as application developer
  to control context switching, introduce idea of coroutines and
  event loops.

- Explain iteration protocol in python, `__next__` and `__iter__`
  magic methods, simple example "Countdown" Class implementing
  the protocol.

- Show equivalent "countdown" generator function using yield
  statement. Discuss generator as a semicoroutine candidate.

- Discuss PEP342 improvements to generators with examples of
  generators using results from yield expressions and the send()
  function.

- Discuss need for delegation to sub-coroutines, incorrect example
  that doesn't handle send() properly, and PEP380 yield from
  syntax.

- Introduce the "asyncio" event loop, give simple examples of
  running on REPL.

- Show solution to animals concurrency example using a generator
  decorated with `asyncio.coroutine` and the aiohttp package.

- Introduce new async/await syntax and the separation of coroutines
  from iterators, the meaning of "awaitable", and revise concurrent
  solution to the animals example using a "native" coroutine.
