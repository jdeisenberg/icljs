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
      
All well and good, but that’s not an entirely realistic scenario. What about a business that bases discount on the quantity purchased? For example, **if** you order less than 50 items, you get a 5% discount; otherwise (when you order 50 or more), you get a 7.5% discount. This is something you haven’t seen yet |---| calculations based on some condition being true or not.

Testing conditions: if
======================

To accomplish tasks like this, you need ClojureScript’s ``if`` function\ [1]_

The model for an ``if`` is:
    
.. parsed-literal::
  
    (if *condition* *true-expression* *false-expression*)
    
The *condition* is some expression whose value is either ``true`` or ``false``.  If the condition is ``true``, the value of the entire expression is ``true-expression``; otherwise, the value is ``false-expression``. Going from this abstract explanation to the concrete example of the discount:
    
::
    
    (if (< qty 50) 0.05 0.075)
    
The expression ``(< qty 50)`` tests to see if ``qty`` is less than 50. If so, the value of the expression is ``true``, so the result of the expressions is 0.05; if not, it’s ``false``, and the value of the expression is 0.075.

.. note::
    If you simply enter an ``if`` expression such as the preceding one into an active code area, you will not see any result. This is due to the way that
    ClojureScript in the browser works. It will do the right thing when used in a program.
    
Let’s see how this works in a program. I have moved the code for calculating the discount into its own function because calculating the discount is really its own separate task. How you figure out what the discount is doesn’t change the formula that uses that amount. Try changing the quantity and see how that affects the total cost.

.. activecode:: discount1
    :caption: Simple Discount
    :language: clojurescript
    
    (defn calc-discount [qty]
       (if (< qty 50) 0.05 0.075))
    
    (defn total-cost [price qty]
      (let [discount (calc-discount qty)]
        (* price qty (- 1 discount))))
      
    (total-cost 10.00 30)


Functions that test conditions
------------------------------

ClojureScript defines these functions for testing conditions. All of the examples shown will evaluate to ``true``.
    
+-----------+-----------------------+-----------------+
| Function  | Means                 | Example         |
+===========+=======================+=================+
| <         | less than             | (< 3 5)         |
+-----------+-----------------------+-----------------+
| <=        | less than or equal    | (<= 19 45)      |
+-----------+-----------------------+-----------------+
| >         | greater than          | (> 17 9)        |
+-----------+-----------------------+-----------------+
| >=        | greater than or equal | (>= 25 25)      |
+-----------+-----------------------+-----------------+
| =         | equal                 | (= 10 (/ 20 2)) |
+-----------+-----------------------+-----------------+
| not=      | not equal             | (not= 17 3)     |
+-----------+-----------------------+-----------------+


Many different conditions: ``cond`` and ``condp``
===================================================

What happens if you decide to have multiple levels of discount, depending upon quantity?

+----------+----------+
| Quantity | Discount |
+==========+==========+
| < 20     | 0%       |
+----------+----------+
| < 50     | 2%       |
+----------+----------+
| < 100    | 5%       |
+----------+----------+
| < 200    | 7.5%     |
+----------+----------+
| >= 200   | 10%      |
+----------+----------+

You can represent it in a flowchart form like this:
    
.. image:: images/nested_if.png
   :alt: Series of diamonds representing the tests needed for evaluating discount per preceding table

    
.. note::
    In the second diamond of the flowchart, you don’t have to ask if the quantity is greater than or equal to 20. You already know that, because the answer to “is it less than 20?” came back as “no” (false).
    
So you *could* write it this way in ClojureScript:
    
::
    
    (defn calc-discount [qty]
      (if (< qty 20) 0
        (if (< qty 50) 0.02
          (if (< qty 100) 0.05
            (if (< qty 200) 0.075 0.10))))) 
        
But that’s really difficult to read, and with a few more choices, the parentheses would get pretty deep. For situations such as this, ClojureScript provides the ``cond`` construct, which is followed by pairs of conditions and values. ClojureScript tests the conditions one at a time and yields the value for the first condition that evaluates to ``true``. Here is what the discount function looks like using ``cond``; try changing the quantity in the function call and see that it works correctly.
    
.. activecode:: cond
    :caption: Using cond
    :language: clojurescript
    
    (defn calc-discount [qty]
      (cond
        (< qty 20) 0
        (< qty 50) 0.02
        (< qty 100) 0.05
        (< qty 200) 0.075
        :else 0.10))
    
    (calc-discount 15)

The value for the last test, ``:else``, is chosen if none of the other conditions came out true.

Compound conditions: ``and`` and ``or``
========================================

This section intentionally left blank.


.. [1] ``if`` is technically not a function. In truth ``if``, ``def``, ``let`` (and others) are classified as *special forms*. ``defn`` is also not a function; it is a *macro*. At this stage, these are distinctions without a difference, but they will become important if you go in depth with ClojureScript. The only reason this footnote is here is so that outraged language purists won’t bombard me with emails about my obvious misclassification of ``if``.