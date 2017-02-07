.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Recursion
::::::::::::::::::::::::::::::::::::::::::::::

Remember back in the preface, where you saw this vector of high and low temperatures?

::

    [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]]
    
When I wanted to create the graph shown in the preface, I had to split the vector into two vectors: one of
high temperatures and one of low temperatures::

    [[3 2 4 4 4 9 16]
    [9 13 10 9 12 20 21]]
    
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


.. activecode:: factorial_1
  :language: clojurescript
  
  (defn factorial [n]
    (if (= n 1) 1
        (* n (factorial (- n 1)))))

  (factorial 5)
  
Advanced Topic: Tail Recursion
================================

We’ll get to the original problem (dividing the list of temperatures) later in this chapter, but there’s an important topic to cover first. If you were to try ``(factorial 50000)``, you would get an error: “Too much recursion.”  To see why this happens, let’s look at the expression ``(* n (factorial (- n 1)))`` when ``n`` is 5. In order to do the multiplication, ClojureScript has to first figure out what ``(factorial (- 5 1))`` works out to, so it has to “wait” until 4! is evaluated.  That calculation, in turn, will have to figure out 3! before it can do *its* multiplication, so it has to wait as well, and so on. Every time this happens, the function has to store its status in an area of memory called the **stack**. That stack has limited room, and once you are out of room, you get the “too much recursion” error. This error also goes by the name “stack overflow.”

There is a way around this problem. If the recursive call is the *very last thing* in the function, then you can use the ``recur`` function to say “do the recursion now,” and ClojureScript will optimize the code so that no stack space is needed for the recursion.  Having the recursion as the very last thing is called **tail recursion**. (In the preceding example, the recursion isn’t the last thing that happens in the function |---| it’s the multiplication).  To do factorials with the recursion as the very last operation, we’ll build a special helper function with two arguments. The first argument is the number whose factorial we want, and the second argument is the “result so far”:
  
.. activecode:: factorial_2
  :language: clojurescript
  
  (defn factorial-helper [n result]
    (if (= n 1)
      result
      (recur (- n 1) (* n result))))
    
  (defn factorial [n] 
      (factorial-helper n 1)) 

  (factorial 50000)
  
The ``factorial-helper`` function will return the result so far if ``n`` is one, otherwise it will use ``recur`` to recursively call itself with ``(- n 1)`` and
``(* n result)`` as the arguments.

Even though the result is a number too large for ClojureScript to represent, we at least get a result rather than an error. Whenever possible, you should try to make your recursive functions tail recursive and use ``recur`` so that you never have to worry about too much recursion.

Recursion and Vectors
========================

You can use recursion to process lists. For example, if you wanted to get the sum of a vector of numbers::
  
  [17 4 26 3] 
  
You already know how to do this with ``reduce`` |---| ``(reduce + 0 [17 4 26 3])``, but you can think of it it as a recursive process. The sum of the entire vector is 17  plus the sum of the remainder of the vector ``[4 26 3]``. The sum of that vector is 4 plus the sum of the rest of *that* vector ``[26 3]`` and so on until you get to an empty vector which means you have added everything up. In other words, recursviely defined, the sum of the entire vector is the result of adding the first element to the sum of the remaining elements.
  
You can use the ``first`` and ``rest`` functions to get the first element and remaining elements in a vector, which lets you write the recursive summation as:
  
.. activecode:: recursive_add
  :language: clojurescript
  
  (defn add-up [numbers]
     (if (empty? numbers)
       0
       (+ (first numbers) (add-up (rest numbers)))))

  (add-up [17 4 26 3])  

The preceding example isn’t tail recursive; again, the addition is the last operation. We can use the helper function trick to allow the use of ``recur``:
  
.. activecode:: tail_recursive_add
  :language: clojurescript
  
  (defn add-helper [result numbers]
    (if (empty? numbers)
      result
      (recur (+ result (first numbers)) (rest numbers))))

  (defn add-up [numbers]
    (add-helper 0 numbers))
  
  (add-up [17 4 26 3])
  
At last! We are ready to accomplish the task we set out at the beginning: splitting the vector of minimum and maximum temperatures into the vector of minimums and the vector of maximums, and we’ll go straight to the tail recursive-with-helper-function solution.

Our result is going to be a vector of two vectors, so, just as we started with 1 for our result in factorial and 0 for adding, the initial result is ``[[][]]``.
The function will start by taking the first item in the temperatures: ``[3 9]``. It will use ``conj`` to append the 3 to the first empty vector in the result, and another ``conj`` to append the 9 to the second empty vector in the result.  It then will recursively call itself with the newly minted result and the remaining items in the tempearture vector. When the temperature vector is empty, our job here is done, and the result is what gets returned.

.. activecode:: tail_recursive_split
  :language: clojurescript
  
  (defn split-temperatures [result temperatures]
     (if (empty? temperatures)
       result
       (let [head (first temperatures)
             min-temp (first head)
             max-temp (last head)]
         (recur [(conj (first result) min-temp)
                 (conj (last result) max-temp)]
          (rest temperatures)))))
         
  (split-temperatures
    [[][]]
    [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])
  
