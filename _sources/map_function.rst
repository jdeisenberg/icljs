..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Manipulating Collections
:::::::::::::::::::::::::

Let’s take the vector of prices ``(def price-vector [3.95 6.80 2.49 5.33 1.99])`` and write a program that will give us a new vector with a 10% discount on each of the prices.
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

Formally defined, the ``map`` function takes two arguments: a function of one parameter, and a collection. ``map`` returns a sequence consisting of the result of applying the function to each item in the collection.

.. note::
    This ``map`` function is not to be confused with the ``map`` collection, which pairs keys and values. Unfortunately, they share the same name, and there’s nothing to be done about it.


Something Important Just Happened
====================================
Up to this point, all of the arguments to functions have been raw data, like numbers and strings.
This is the first time you have seen a function as an argument to another function. I deliberately used the ``(def)`` form instead of ``(defn)`` to remind you that you can bind a function to a symbol, just as you can bind numbers or strings or lists to symbols. In ClojureScript, functions may be considered as just another type of data that you can bind to symbols and pass to and from other functions. That’s exactly what has happened here: I passed the ``discount`` function as an argument to the ``map`` function.

When you have a function like ``map`` that takes another function as an argument, it is referred to as a *higher-order function*.
(If a function returns another function as a result |---| yes, this is possible |---| it is also a higher-order function.

Exercises
=========

.. container:: full_width

    .. tabbed:: circle_area

        .. tab:: Your Program

            Write a program that uses ``map`` to convert the ``radius-vector`` to a sequence of circle areas. You will write a function named ``calculate-area`` that calculates the area of a circle given its radius, then use it as the first argument to ``map``. You can use ``js/Math.PI`` for the value of pi. For extra bonus points, have the program create a vector as its result. (Hint: ``into``)

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

.. container:: full_width

    .. tabbed:: price_rounding

        .. tab:: Your Program

            Write a program that uses ``map`` to convert the ``price-vector`` to a sequence of prices that have been rounded up to the nearest 10-cent value. Thus, for the given vector, your result should be (4 6.8 2.5 5.4 2) Write a function named ``round-up-price`` that takes a single price as its argument and returns the result rounded up. For extra bonus points, have the program create a vector as its result. (Hint: ``into``). Most of your thinking in this exercise will probably go into figuring out how to do the rounding; the ``map`` part is entirely straightforward.

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
