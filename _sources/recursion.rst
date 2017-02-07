.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Recursion
::::::::::::::::::::::::::::::::::::::::::::::

Remember back in the preface, where you saw this vector of high and low temperatures?

::

    [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]]
    
When I wanted to create the graph shown in the preface, I had to split the vector into two vecctors: one of
high temperatures and one of low temperatures::

    [3 2 4 4 4 9 16]
    [9 13 10 9 12 20 21]
    
While it is possible to use ``reduce`` to accomplish this goal, let’s investigate a technique called *recursion* to solve this problem. Recursion happens when a function calls itself. You can think of it as the programming equivalent of the `Droste Effect`_, where a picture contains a smaller version of itself.

.. _Droste effect: https://en.wikipedia.org/wiki/Droste_effect

To quote Wikipedia, “The woman in the 1904 Droste cocoa package holds two objects bearing smaller images of herself holding the same objects, and so on recursively.” This series of ever-smaller images appears to go on forever. The key word here is *appears*, because the smaller images eventually stop when they become to small to draw. This is a good thing, otherwise the artist would still be drawing it!

As a first example of recursion, I’m going to show you how to compute factorials. This pains me greatly, as it is the example that *everyone* uses, and I hate to join the crowd, but the fact is that it’s a good example for helping you wrap your head around the idea of recursion.

The factorial of an integer is represented by the exclamation mark and is the product of all the positive integers up to and including the integer in question::

    1! = 1
    2! = 2 × 1
    3! = 3 × 2 × 1
    4! = 4 × 3 × 2 × 1
    
and so on. You may be wondering why anyone would ever use this; it turns out to be very handy for figuring out problems involving probabilities.  Now let’s add a few parentheses and reverse the order of the example, to see something interesting::

    4! = 4 × (3 × 2 × 1) = 4 × 3!
    3! = 3 × (2 × 1) = 3 × 2!
    2! = 2 × (1) = 2 × 1!
    1! = 1
    
Each factorial can be defined in terms of yet another factorial |---| until you get down to 1, which stops the process from going on forever. In general, then, *n*! can be defined as *n* × (*n* - 1)! where *n* is greater than 1. The important part is that 1! is *not* defined in terms of itself. That’s the “stopping point”; the equivalent of where the images get too small to keep drawing, and thus ending the recursion.


.. activecode:: map_square
  :language: clojurescript
  
  (defn factorial [n]
    (if (= n 1) 1
        (* n (factorial (- n 1)))))

  (factorial 5)
  




