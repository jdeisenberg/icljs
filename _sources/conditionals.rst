..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Conditionals
:::::::::::::::::::::::::::::::

Consider the following function, which, given a price and quantity, calculates a total cost with a 5% discount:
    
::
    
    (defn total-cost [price qty]
      (let [discount 0.05]
        (* price qty (- 1 discount))))
      
All well and good, but that’s not an entirely realistic scenario. What about a business that bases discount on the quantity purchased? For example, **if** you order less than 100 items, you get a 5% discount; otherwise (when you order 100 or more), you get a 7.5% discount. This is something you haven’t seen yet |---| calculations based on some condition being true or not.

Testing conditions: if
======================

To accomplish tasks like this, you need ClojureScript’s ``if`` function\ [1]_

The model for an ``if`` is:
    
.. parsed-literal::
  
    (if *condition* *true-expression* *false-expression*)
    
The *condition* is some expression whose value is either ``true`` or ``false``.  If the condition is ``true``, the value of the entire expression is ``true-expression``; otherwise, the value is ``false-expression``. Going from this abstract explanation to the concrete example of the discount:
    
::
    
    (if (< qty 100) 0.05 0.075)
    
The expression ``(< qty 100)`` tests to see if ``qty`` is less than 100. If so, the value of the expression is ``true``; if not, it’s ``false``.

Functions that test conditions
------------------------------

Watch this space.

Many different conditions: ``cond`` and ``condp``
================================================

To be written.

Compound conditions: ``and`` and ``or``
========================================

This section intentionally left blank.


.. [1] ``if`` is technically not a function. In truth ``if``, ``def``, ``let`` (and others) are classified as *special forms*. ``defn`` is also not a function; it is a *macro*. At this stage, these are distinctions without a difference, but they will become important if you go in depth with ClojureScript. The only reason this footnote is here is so that language purists won’t bombard me with outraged emails about my obvious misclassification of ``if``.