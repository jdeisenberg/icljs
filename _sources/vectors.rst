..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Vectors
'''''''''

A vector is a series of items inside square brackets. You have seen vectors when you define functions; the parameter names are a vector.  
Vectors are normally the choice for related items rather than lists. Consider this vector of prices:

.. activecode:: price-vector
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (println price-vector)

Fundamental Operations
==========================

Again, look at the following operations that work on all collections, which includes vectors:

* ``first`` returns the first items in the collection
* ``rest`` returns a sequence of all the items except the first one
* ``last`` returns the last item in the collection
* ``count`` gives you the number of items in the collection
* ``vector?`` returns ``true`` if its argument is a vector, ``false`` otherwise
* ``conj`` takes a collection and an item, and returns a new collection with that element added to the collection.

In the case of vectors, ``conj`` puts the new element at the **end** of the vector that it returns.  Try these expressions in the following active code box, or use a series
of ``println`` to do them all at once; for your convenience, the ``price-vector`` vector has been defined.

::

    (first price-vector)
    (rest price-vector)
    (count price-vector)
    (vector? price-vector)
    (conj price-vector 7.86)

.. activecode:: try-lists
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])

Remember that the result of all of these functions is a brand new vector; the original vector is immutable and remains untouched.

When you tried ``(rest price-vector)``, you may have noticed that the output did *not* have square brackets: the result was ``(6.8 2.49 5.33 1.99)``  That is because the result of the ``rest`` function is a *sequence*, as shown by the ``type`` function:

.. activecode:: rest-seq
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (type (rest price-vector))

You can convert a sequence (or a list) into a vector by using the ``into`` function. The first argument to ``into`` is the destination collection. In the following example, that is an empty vector ``[]``. The second argument is the collection or sequence to be inserted *into* the destination:

.. activecode:: into-vector
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (def remainder (rest price-vector)) ; this is a sequence
    (def rem-vector (into [] remainder))
    (println rem-vector)
    (println (type rem-vector))

There are two ways to access any arbitrary element in a vector. You can, as with lists, use the ``nth`` function, which takes a vector as its first argument and an index number as its second argument, where zero is the index of the first item in the vector. What happens if you give a negative number or a number greater than or equal to the number of items in the list? Try different index numbers and find out:

.. activecode:: try-nth-vector
    :language: clojurescript   

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (nth price-vector 0)

Or, if you wish, you can use the symbol as if it were a function and follow it with the index number:

.. activecode:: vector-as-function
    :language: clojurescript

    (def price-vector [3.95 6.80 2.49 5.33 1.99])
    (price-vector 0)

OK, enough of this background |---| when are we going to actually *do* something with these collections? On the next page, that’s when.
