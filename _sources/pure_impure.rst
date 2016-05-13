..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Pure and Impure Functions
:::::::::::::::::::::::::::

Almost all of the functions you have seen to this point are *pure* functions: given the same input, they always
give you the same output. This is very much what you would expect from mathematical functions; when you take
the square root of 36 you expect a result of 6 every time. (If you ever got back an answer of 7.3, you would
be in some alternate universe twilight zone.)

This is a pure function in ClojureScript:
    
::
    
    (defn average [a b]
      (/ (+ a b) 2.0))

If you call ``(average 5 17)`` you will get back 11 as your answer. The good news is that your function is reliable;
you don’t care what other functions do with their parameters; they can’t interfere with you. The bad news is that
if you want the average of two different numbers, you have to rewrite the function call.

When you think of it, if you only had pure functions, you could never do input or output. Consider this function,
which takes an HTML ``<input/>`` field’s ``id`` as its argument and returns the value in that field as a floating point
number:
    
::
    
    (defn float-value [field-id]
     (let [input-element (.getElementById js/document field-id)]
       (js/parseFloat (.-value input-element))))
     
If you want the value that the user has typed into an ``<input type="text" id="price"/>``, you would call:
    
::
    
    (float-value "price")
    
This is not a pure function; the result is not going to be the same every tme you make the call; in fact,
it will almost *never* be the same, as it depends on the user’s input. Other examples of impure functions are
functions that generate random numbers or get the current time of day. You *never* want them to return the same
value for the same input!

Similarly, output is not pure, in the sense that there is no real “return value” from the ``(println ...)`` function that
was used in the :doc:`explanation of symbols </symbols>`. Unlike ``(average)``, it doesn’t give back a value you can
use in further calculations; we only love it for its *side effect* of putting output on the screen. (FYI, an
expression like ``(println "It works")`` returns a value of ``nil``.)

In short: pure functions provide the same output for the same input, never alter any values outside their walls, and
have no side effects. Impure functions don’t.

Any program you write will have both kinds of functions. In general, the best approach is to separate the impure parts of your
programs (the input and output) from the processing of the data, which is usually pure.




