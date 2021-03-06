# PythonConcurrencyTalk

Examples, resources, slides, and outline for my python concurrency
and coroutines talk.

**Presentations of this talk*:**

This repository is organized with a release for each instance where
the talk was given, in case anyone would like to reference the talk
as it was at that time. However, I generally consider the current
version to be a better general reference.

* [PyTennessee Conference February 4, 2017](https://www.pytennessee.org/schedule/presentation/131/) - current version

* [PyNash Meetup September 29, 2016](https://www.meetup.com/PyNash/events/233675647/) - Tag: [PyNash-2016-08-29](https://github.com/appeltel/PythonConcurrencyTalk2016/tree/PyNash-2016-08-29)


### Title

A brief introduction to concurrency and coroutines

### Synopsis

This is a beginner-friendly introduction to concurrent programming
Using a simple example task, differences in threaded
and cooperative approaches to concurrency will be illustrated.
The talk will then focus on how coroutines have developed in
Python from iteration protocol and generators to the new
async/await syntax, and how coroutines
can be used with the provisional "asyncio" event loop in the Python
standard library. It will be assumed that the listener has a basic
understanding of functions, classes, and exceptions in Python, but
no prior knowledge of concurrent programming is required.

### Outline as Presented 

- Explain the difference between concurrency and parallelism using
  the example of cooking a traditional US Thanksgiving dinner.

- Motivate with example task of retrieving animal noises from the slow
  animals API and printing them using animation. Discuss difference
  between parallelism and concurrency, need for the latter in this
  situation.

- Explain iteration protocol in python, `__next__` and `__iter__`
  magic methods, simple example "Countdown" Class implementing
  the protocol.

- Show equivalent "countdown" generator function using yield
  statement. Discuss generator as a semicoroutine candidate.

- Discuss PEP342 improvements to generators with examples of
  generators using results from yield expressions and the send()
  function.

- Discuss need for delegation to sub-coroutines and PEP380 yield from
  syntax.

- Introduce new async/await syntax, the separation of coroutines
  from iterators, and the meaning of "awaitable"

- Introduce the "asyncio" event loop, give simple examples of
  running on REPL.

- revise concurrent solution to the animals example using coroutines
  and asyncio.

### Extended Offline Presentation

The actual slides alone don't constitute a resource that one can
reasonably follow to understand the talk. I'm working on a set of
articles below which explain the basics of concurrency and coroutines
in python, along with some extended information that I would have talked
about if I had an infinite amount of time to prepare and present the
talk:

1. [What is concurrency?](talk/concurrency.md)
2. [Coroutines versus threads](talk/threads.md) (optional/extended)
3. [Python on the road to coroutines](talk/generators.md) (optional)
4. [Using coroutines with asyncio](talk/coroutines.md)
5. [Writng an asyncronous webservice](talk/webservice.md) (extended)

Sections marked optional are not really needed if you want to get
started using asyncio and coroutines, but give some extra information
on how they are implemented and why one might use them as opposed to
other approaches.

Sections marked extended were not presented in the talk.

### Link to Slides

[presentation slides](pytn17_slides.pdf)
