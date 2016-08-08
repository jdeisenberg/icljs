..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Manipulating Collections 
::::::::::::::::::::::::::

The previous two pages gave you the fundamentals of lists and vectors, but if you think there was something missing, you are correct
You may have een wondering how you work with the items in a collection one after another.  In this page and the next pages, we will show you three of the most important functions for manipulating collections:  ``map``, ``reduce``, and ``filter``.


The ``map`` function
=======================

You use ``map`` when you want to create a new collection by applying a function to each element of a collection.
For example, let’s take the vector of prices ``(def price-vector [3.95 6.80 2.49 5.33 1.99])`` and write a program that will give us a new vector with a 10% discount on each of the prices.
You already know how to do this for a single price:

::

    (defn discount [price]
      (* price 0.90))

What you now need is some way to apply that function to each of the items in ``price-vector``. The ``map`` function does exactly that.

.. activecode:: map-discount
    :caption: Mapping a function over a vector
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (def discount (fn [price]
        (* price 0.90)))

    (map discount price-vector)

The ``map`` function takes two arguments: a function of one parameter, and a collection. In this example, the function is the ``discount`` function, and ``price-vector`` is the collection.

.. note::
    This ``map`` function is not to be confused with the ``map`` collection, which pairs keys and values. Unfortunately, they share the same name, and there’s nothing to be done about it.

Here is a short video that may help as well:
    
.. youtube:: RtUjaxqmaDI
    :height: 315
    :width: 560
    :align: center

Something Important Just Happened
====================================
Up to this point, all of the arguments to functions have been raw data, like numbers and strings.
This is the first time you have seen a function as an argument to another function. I deliberately used the ``(def)`` form instead of ``(defn)`` to remind you that you can bind a function to a symbol, just as you can bind numbers or strings or lists to symbols. In ClojureScript, functions may be considered as just another type of data that you can bind to symbols and pass to and from other functions. That’s exactly what has happened here: I passed the ``discount`` function as an argument to the ``map`` function.

When you have a function like ``map`` that takes another function as an argument, it is referred to as a *higher-order function*.
(If a function returns another function as a result |---| yes, this is possible |---| it is also a higher-order function.)

Exercises
=========

**Exercise 1:** Write a program that uses ``map`` to convert the ``radius-vector`` to a sequence of circle areas.
You will write a function named ``calculate-area`` that calculates the area of a circle given its radius, then use it as the first argument to ``map``. You can use ``js/Math.PI`` for the value of pi. For extra bonus points, have the program create a vector as its result. (Hint: ``into``)

.. container:: full_width

    .. tabbed:: circle_area

        .. tab:: Your Program

            .. activecode:: circle_area_q
                :language: clojurescript

                (def radius-vector [3 1.5 4])
                ; your code here


        .. tab:: Answer

            .. activecode:: circle_area_answer
                :language: clojurescript

                (def radius-vector [3 1.5 4])
                (defn calculate-area [radius]
                    (* js/Math.PI radius radius))

                (into [] (map calculate-area radius-vector))

**Exercise 2:** Write a program that uses ``map`` to convert the ``price-vector`` to a sequence of prices that have been rounded up to the nearest 10-cent value.
Thus, for the vector ``[3.95 6.80 2.49 5.33 1.99]``, your result should be ``(4 6.8 2.5 5.4 2)`` Write a function named ``round-up-price`` that takes a single price as its argument and returns the result rounded up. For extra bonus points, have the program create a vector as its result. (Hint: ``into``).

Remember in the :doc:`interlude <what_is_programming>` I sang the praises of planning. This is one of those cases. Figuring out how to round 33 cents up to 40 cents, but keeping 30 cents as 30 cents takes a bit of thought and planning. 

.. container:: full_width

    .. tabbed:: price_rounding

        .. tab:: Your Program

           .. activecode:: price_rounding_q
                :language: clojurescript

                (def price-vector [3.95 6.80 2.49 5.33 1.99])
                ; your code here


        .. tab:: Answer

            To round up the price, convert the price to cents by multiplying by 100. To get an even multiple of 10, do an integer division by 10, then multiply by 10. 
            However, that rounds *down* rather than up; a number like 34 would go to 30 rather than 40. The trick is to add 9 to the original number before rounding down.
            When you do that, a number like 30 |---| which is already a multiple of 10 |---| becomes 39, which rounds back down to 30; but 32 would go up to 41, which rounds down to 40, effectively rounding 32 *up* to 40, the desired result.

            .. activecode:: price_rounding_answer
                :language: clojurescript

                (def price-vector [3.95 6.80 2.49 5.33 1.99])

                (defn round-up-price [price]
                    (let [cents (* price 100)
                          added (+ 9 cents)
                          rounded (* 10 (quot added 10))]
                        (/ rounded 100)))

                (into [] (map round-up-price price-vector))

.. _anonymous-functions:

``map`` Shortcut #1: Anonymous Functions
=============================================

If the function you are using in ``map`` is short (as it is in the example with the discount and the circle areas), you don’t have to create a new, named function.
Instead, you can define the function right in the call to ``map``.  Here is the discount example, using an *anonymous function* (a function that isn’t bound to a symbol).

.. activecode:: map-anonymous
    :caption: Using an anonymous function with map
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])

    (map (fn [price] (* price 0.90)) price-vector)
    
Now give it a try. Convert the circle area example to use an anonymous function. As before, your goal is a program that uses ``map`` to convert the ``radius-vector`` to a sequence of circle areas.
    
.. container:: full_width

    .. tabbed:: circle_area_anonymous

        .. tab:: Your Program

            .. activecode:: circle_area_anonymous_q
                :caption: Anonymous Function Exercise
                :language: clojurescript

                (def radius-vector [3 1.5 4])
                ; your code here


        .. tab:: Answer

            .. activecode:: circle_area_anonymous_answer
                :caption: Anonymous Function Exercise Answer
                :language: clojurescript

                (def radius-vector [3 1.5 4])

                (into [] (map (fn [radius] (* js/Math.PI radius radius)) radius-vector))
                
``map`` Shortcut #2: Even Shorter Function Syntax
=====================================================

You can define an anonymous function in a *very* compact manner. For a function with one parameter, which is what we are using here:
    
* Drop the ``fn`` and parameter list altogether
* Put a ``#`` before the opening parenthesis
* Use ``%`` in place of the parameter.

Here is the price discount program again, in the short syntax:
    
.. activecode:: map-anonymous2
    :caption: Using a short syntax anonymous function with map
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])

    (map #(* % 0.90) price-vector)
    
You can use this shortcut syntax for functions with more than one parameter; you use ``%1`` to stand for the first parameter, ``%2`` for the second, and so on. You could
write the ``average`` function with two parameters as follows. The long form is shown first as a comment for reference.
    
.. activecode:: average-short-syntax
    :caption: Multiple parameter short syntax function
    :language: clojurescript

    ; (def average (fn [a b] (/ (+ a b) 2.0)))
    (def average #(/ (+ %1 %2) 2.0))

    (average 7 12)
    
Which Shortcut Should You Use?
================================

When you are learning a foreign language, there are three classes of phrases:
    
* Phrases you have to know how to say and recognize
* Colloquial phrases that you may use if you feel confident about it
* Phrases you should be able to understand but not be expected to produce on your own

That’s how I feel about writing functions for use with ``map``:

* Defining a separate named function always works, and, if you are a beginning programmer, may be the clearest way to express your intention. For a longer function such as the price rounding function, this is almost certainly your best option.
* For very short functions, if you feel comfortable using an anonymous function with ``fn``, go for it.
* You may find that the ultra-short syntax borders on unreadability, so you don’t have to use it. Just be aware that other programmers are greatly enamored of it, so you will have to recognize it in their code.
    
