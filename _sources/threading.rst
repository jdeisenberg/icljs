..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Threading Function Calls
::::::::::::::::::::::::::::

At some point, you will be writing sequences of collection-processing functions. Presume,
for some reason, you wanted the sum of all squared integers that are less than 1000 and divisible by four.

Here is code that will work, using the ``range`` function, which generates a sequence of numbers from zero up to but not including the number you specify:
    
.. activecode:: nested_calls
    :caption: Nested calls
    :language: clojurescript
    
    (defn multiple-of-four? [value]
        (= (rem value 4) 0))
        
    (defn square [x] (* x x))
    
    (reduce +
       (filter multiple-of-four?
          (map square (range 33))))

This, in fact, mirrors the way it was described in English, but you can also see that you have to write the expression from the “inside out”.  You can write the same expression using the ``->>`` threading operator. The ``->>`` operator takes two or more arguments. The first argument is a list, which is used as the *last* item in the second argument, which is an expression. If there are more arguments, the result of the second expression is used as the last item of the third argument, and so on. In other words, the original list “threads” its way through the expressions, always as the last item.  This lets you rewrite the preceding code as follows:
    
.. activecode:: threaded_calls
    :caption: Threaded calls
    :language: clojurescript
    
    (defn multiple-of-four? [value]
        (= (rem value 4) 0))
        
    (defn square [x] (* x x))
    
    (->> (range 33)
         (map square)
         (filter multiple-of-four?)
         (reduce +))

This is more in line with a description of the algorithm as “Take the numbers 0 to 32, square them, get only the multiples of four, and add them up.”

Use whichever method makes the algorithm more clear to you; that will make it clear to other people |---| and when you come back to code you wrote a few months ago, *you* will be “other people.”

.. reveal:: reveal_singlethread
    :showtitle: Learn about the -> form
    :hidetitle: Hide Information
    
    There is also a ``->`` form, known as “thread first”; it works the same as ``->>`` except it inserts the list as the first item in the subsequent expressions.

