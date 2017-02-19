# Part 1: What is Concurrency?

This section explores what is meant by the term "concurrency" and
how this differs from parallelism.

The Animals API and a simple application using it is also introduced.
This simple API will be used throughout this tutorial to demonstrate
how to use coroutines in python.

## Cooking Thanksgiving Dinner

Actual cooking is a good example to use to understand concurrency as
when people cook, they actually use a form of concurrency. In making
a Thanksgiving dinner, one will typically have a number of recipes,
one for each dish. One might for example, have a recpie for roast
turkey, a recipe for apple pie, a recipe for cranberry sauce, a recipe
for mashed potatoes, and so on. One could even imagine writing the
task of cooking Thanksgiving dinner as a python program, where each
recipe is a function or subroutine:

    def make_thanksgiving_dinner():
        """
        Make a delicious dinner!
        """
        make_roast_turkey()
        make_mashed_potatoes()
        make_cranberry_sauce()
        make_apple_pie()
        ...

If someone actually cooked following such a program, they would complete
each dish before moving on to the next one. That would mean that you
prepare the turkey first, and do not start the mashed potatoes until the
turkey is finished. This would result in a large portion of wasted time
where the cook would simply stare at the oven timer for half an hour
waiting for the next time to baste the turkey. This time is wasted because
the cook is only dealing with one recipe at a time, and each recipe
includes periods of time where one must simply wait for something to finish
baking, heat up, or come to a boil. This is an example of _sequential_
excecution of recipes.

In reality, what most people will do is use the wasted periods of time
in one recipe to get started on other ones. For example, after one puts
the turkey in the oven, one might start peeling the potatoes and get the
water boiling. Then while the potatoes boil, one can start slicing apples
for the pie. This is an example of concurrent execution. The cook is in the
middle of completing several recipes, and switches from executing one
to another when there is a convenient waiting period. The ability to deal
with multiple things going on at the same time is _concurrency_.

Notice that the cook in concurrently executing multiple recipes is never
actually doing multiple things at the same time. Many things may be
happening around the cook, such as water heating and turkey roasting in the
oven, but the attention of the cook is always focused on a single task
like peeling potatoes or slicing apples. If there is too much actual work that
needs to be done in order to get dinner ready, the cook might call over a
friend to help, perhaps by peeling potatoes while the cook slices apples.
This enlisting of multiple people to actually do work at the same time is
an example of _parallelism_.

In an actual program, one may need parallel execution if the amount of
computational work to be done is large and the time required for a single
CPU core is unacceptably long. But in many cases there is very little
computational work to be done, but multiple long delays waiting for
interactions with network databases or other resources. In this latter case
using concurrency, or dealing with multiple network interactions going on
at the same time, can greatly speed up execution of a program without
requiring parallel execution on multiple CPU cores.
