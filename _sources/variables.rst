..  Copyright © J David Eisenberg and O'Reilly Media
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Variables
:::::::::

Doing arithmetic with concrete numbers is fine, but when you move from algebra to arithmetic, you use variables so that you can manipulate abstract symbols. Similarly, in ClojureScript, you will want to be able to describe transformations of data in abstract terms, and variables help you do this.

How to Define a Variable
========================

To define a variable, you use the ``def`` function. It takes two arguments: the name of the
variable you wish to define, and the value of the variable. Once a variable is defined,
you can use it in expressions, including definitions of other variables.

.. activecode:: variable_def
    :caption: Define Variables Here
    :language: clojurescript
    
    (def years 62)
    (def days (* 365 years))
    days

What’s in a (Variable) Name?
===============================

Variable names, also called *symbols*, must start with a non-numeric character, followed by letters, digits, or any of \*, +, !, -, _, ', and  ?.
    
Making variable names meaningful is an important part of programming.  If, instead of using ``years`` I had used ``y``, the code wouldn’t be as clear; ``y`` could also refer to a graphical *y*-coordinate.

Sometimes you might have a variable name that is best described by two words, such as an interest rate. Just calling it ``rate`` is not good; a financial program could have interest rates, penalty rates, or any number of types of rates. You can’t call it ``interest rate`` because you can’t put spaces in a variable name. There are three ways that people solve the problem of writing multi-word variable names:
    
* ``interestRate`` This is called *camel case*, where every word after the first begins with a capital letter (named because the capital letters are distantly reminiscent of a camel’s humps)
* ``interest_rate`` In this method, words are separated by underscores
* ``interest-rate`` Words are separated by hyphens. This is what you will see most often in ClojureScript.

Again, in terms of meaningfulness, a name like ``ir`` would be far too short, and ``interest-rate-calculated-on-a-per-month-basis`` would be ridiculously long.

.. reveal:: var_reveal_1
    :showtitle: See extra info
    :hidetitle: Hide extra info

    ClojureScript’s rules for variable names give you a great deal of power.
    You can abuse that power by writing confusing code like this:
        
    .. activecode:: variable_def2
        :caption: How to Ruin Your Life
        :language: clojurescript
        
        (def def 2)
        (def + 3)
        (def - 4)
        (* def (/ + -))

    Or you can use that power wisely. For example, by “letter,” ClojureScript doesn’t just mean A through Z;
    you can use alphabetic characters in any language. Here’s
    the first example with the variable names in Russian:

    .. activecode:: variable_def3
        :caption: Variables aren’t just A-Z
        :language: clojurescript
        
        (def лет 62)
        (def дней (* лет 365))
        дней
        

You Try It
----------

Give this a try: define a variable named ``hours`` and another named ``minutes``. Set them to any values you like. Then define a third variable named ``total-minutes`` that is set to 60 times ``hours``, plus ``minutes``.

.. tabbed:: variable_def4

    .. tab:: Question
    
        .. activecode:: variable_def3
            :above
            :language: clojurescript

            ; Your code here

    .. tab:: Answer

        .. activecode:: arithmetic_exercises
            :above
            :language: clojurescript
            
            (def hours 3)
            (def minutes 54)
            (def total-minutes (+ (* hours 60) minutes))
            total-minutes
