.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Recursion
::::::::::::::::::::::::::::::::::::::::::::::
    
Recursion happens when a function calls itself. You can think of it as the programming equivalent of the `Droste Effect`_, where a picture contains a smaller version of itself.

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

If you were to try ``(factorial 50000)``, you would get an error: “Too much recursion.”  To see why this happens, let’s look at the expression ``(* n (factorial (- n 1)))`` when ``n`` is 5. In order to do the multiplication, ClojureScript has to first figure out what ``(factorial (- 5 1))`` works out to, so it has to “wait” until 4! is evaluated.  That calculation, in turn, will have to figure out 3! before it can do *its* multiplication, so it has to wait as well, and so on. Every time this happens, the function has to store its status in an area of memory called the **stack**. That stack has limited room, and once you are out of room, you get the “too much recursion” error. This error also goes by the name *stack overflow*.

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

The preceding example isn’t tail recursive because the addition is the last operation. We can use the helper function trick to allow the use of ``recur``:
  
.. activecode:: tail_recursive_add
  :language: clojurescript
  
  (defn add-helper [result numbers]
    (if (empty? numbers)
      result
      (recur (+ result (first numbers)) (rest numbers))))

  (defn add-up [numbers]
    (add-helper 0 numbers))
  
  (add-up [17 4 26 3])
  
Strings as Collections
======================================

The exercise for this chapter depends on being able to manipulate strings. It turns out that you can treat a string of characters, to a large extent, as if it were a sequence of characters. Try this:

.. activecode:: strings_as_sequences
    :language: clojurescript
    
    (def s "abcdefg")
    (js/alert (count s))
    (js/alert (first s))
    (js/alert (rest s))
    
Note that ``rest`` returns a sequence of characters. If you want to gather all of the items in the sequence back into a single string, you can ``apply`` the ``str`` function to all the characters (try it in the preceding activecode)::

    (apply str (rest s))
    
Recursion: Palindrome tester
===============================

You can now use recursion to write a function named ``is-palindrome?`` that takes a string as its parameter. If the string is a palindrome (it reads the same backwards and forwards), the function returns ``true``, otherwise ``false``. Thus, ``(is-palindrome? "peep")`` and ``(is-palindrome? "rotor")`` are ``true`` while ``(is-palindrome? "robber")`` is ``false``.

How can you use recursion to tell if something is a palindrome? Let’s examine *rotor*. The first and last letters match, so we discard them and are left with *oto*. Is that a palindrome? (There’s the recursion) Its first and last letters match, so we discard them and are left with *t*, which, being only one letter, is a palindrome.  The same goes for *peep*. The first and last letters match, so we discard them and are left with *ee*. Again, we ask if the first and last letters match. They do, so we discard them, and we are left with nothing, which is the same backwards as forwards.

The word *robber* isn't a palindrome: The first and last letters match, so we discard them, and are left with *obbe*. The first and last letters do **not** match, so the word isn’t a palindrome.

Here’s the logic:

* If the length of the string (using ``count``) is zero or one, we have a palindrome. This is the **end case**, which prevents infinite recursion.
* Otherwise
    * if the first and last letters match,
        * See if everything else is a palindrome. This is where the recursion is. (Hint: use ``butlast`` and ``rest``)
        * otherwise it’s not a palindrome

.. container:: full_width

    .. tabbed:: palindrome_area

        .. tab:: Your Program

            .. activecode:: palindrome_q
                :language: clojurescript

                (defn is-palindrome? [s]
                  ; your code here
                  )
                
                (is-palindrome? "rotor")

        .. tab:: Answer

            .. activecode:: palindrome_answer
                :language: clojurescript

                 (defn is-palindrome? [s]
                    (if (<= (count s) 1)
                      true
                      (if (= (first s) (last s))
                        (recur (butlast (rest s)))
                        false)))
                
                (is-palindrome? "rotor")

A Better Palindrome Tester
============================

The preceding function works fine, but it would be nice to be able to test for sentences like “A man, a plan, a canal - Panama!” or “Madam, I’m Adam.”  In order to do this, you would want to convert the string to all lower case and get rid of anything that isn’t a letter.  You can use ``.toLowerCase`` to do the first part. Keeping only letters is a perfect job for ``filter`` once you know how to test if a character is between ``"a"`` and ``"z"`` inclusive. You can’t do this::

  (def ch "p")
  (and (>= ch "a") (<= ch "z"))
  
because ``>=`` and ``<=`` expect numbers. However, you can use the ``compare`` function.  ``compare`` returns a negative number if its first argument is less than its second argument, zero if they are equal, and positive if the first argument is greater than the second argument.  Thus::

  (compare 3 5) ; returns -1
  (compare 5 5) ; returns 0
  (compare 7 5) ; returns 1
  (compare "a" "c") ; returns -1
  (compare "x" "t") ; returns 1
  
So, you can see if a character is a letter (at least for English) with a test like this::

  (and (>= (compare ch "a") 0) (<= (compare ch "z") 0))
  
Given this information, see if you can improve the palindrome function by converting to lower case, filtering to keep letters only, and then using the existing ``is-palindrome?`` function. Hint: you can use threading ``->>`` to make your code more readable.

.. container:: full_width

    .. tabbed:: palindrome2_area

        .. tab:: Your Program

            .. activecode:: palindrome2_q
                :language: clojurescript

                (defn is-palindrome? [s]
                  ; previous code goes here
                  )
                
                (defn better-palindrome [s]
                  ; this will call is-palindrome?
                  )
                  
                (better-palindrome "Madam, I'm Adam.")

        .. tab:: Answer

            .. activecode:: palindrome2_answer
                :language: clojurescript
                
                (defn is-letter? [ch]
                    (and (>= (compare ch "a") 0) (<= (compare ch "z") 0)))

                 (defn is-palindrome? [s]
                    (if (<= (count s) 1)
                      true
                      (if (= (first s) (last s))
                        (recur (butlast (rest s)))
                        false)))
                        
                (defn better-palindrome [s]
                  (->> s .toLowerCase
                         (filter is-letter?)
                         is-palindrome?))
                         
                (better-palindrome "Madam, I'm Adam.")
