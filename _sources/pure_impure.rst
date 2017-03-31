..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Pure and Impure Functions
''''''''''''''''''''''''''

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
functions that generate random numbers or get the current day and time. You certainly do not want these to
return the same value every time you call them!

Similarly, output is not pure, in the sense that there is no real “return value” from the ``(println ...)`` function that
was used in the :doc:`explanation of symbols </symbols>`. Unlike ``(average)``, it doesn’t give back a value you can
use in further calculations; we only love it for its *side effect* of putting output on the screen. (FYI, an
expression like ``(println "It works")`` returns a value of ``nil``.)

In short: pure functions provide the same output for the same input, never alter any values outside their walls, and
have no side effects. Impure functions don’t.

Immutability
=============

Going hand in hand with pure functions is the concept of *immutability*; once a symbol is bound to a value, that value does not
change. For example, in algebra, when you say *x* = 5 and then  *y* = *x* + 3, the 5 is transformed to a new value, but
the number 5 itself does not change, and *x* still stands for 5.

Similarly, in ClojureScript, functions generally do not modify their arguments (but see the following section for exceptions).
This means you can call functions with the confidence that they will not stomp all over your carefully constructed bindings.

In the :doc:`example of accessing web page data </web_pages>`, you can see the ``(set!)`` function, which changes the value that
is bound to the ``.-innerHTML`` property of a paragraph on the web page. The exclamation point is a convention in ClojureScript
that warns you that the function is impure and modifies its arguments.

Dealing with Impurity
======================

At some point, you will have to deal with the outside world, and you may have to interact with JavaScript, which does
not have strict ideas of function purity and immutability. This means that any program you write will have to have
impure functions and change the state of JavaScript *variables* (named memory locations). In general, the best approach
is to separate the impure parts of your programs (the input and output) from the processing of the data, which is usually pure.
Confine them to their own functions, clearly labeled as such, and your job of updating and maintaining your programs will be
easier.




