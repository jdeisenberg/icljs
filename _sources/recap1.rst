..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Quick Review 1
'''''''''''''''
    
Expressions
===========

ClojureScript programs consist of expressions. An expression is made up of an open parenthesis, a function name, the function’s arguments, and a closing parenthesis.
You may nest expressions as deeply as you wish, though the more deeply you nest them, the harder your code may be to read and understand.

Examples:
    
* ``(+ 3 5)``
* ``(* 3 (+ 4 5))``
* ``(/ (+ 3 4) (* (- 5 6) (+ 7 8)))``

Arithmetic Functions
====================

Here are the arithmetic functions:
    
+--------------+------------------------------+
| **Function** | **Meaning**                  |
+==============+==============================+
| ``+``        | Addition                     |
+--------------+------------------------------+
| ``-``        | Subtraction                  |
+--------------+------------------------------+
| ``*``        | Mutiplication                |
+--------------+------------------------------+
| ``/``        | Division                     |
+--------------+------------------------------+
| ``quot``     | Quotient (integer division)  |
+--------------+------------------------------+
| ``rem``      | Remainder (integer division) |
+--------------+------------------------------+
    
Arithmetic functions other than ``quot`` and ``rem`` can take more than two arguments:
    
* ``(+ 3 4 5)`` evaluates to 12
* ``(- 10 3 2)`` evaluates to 5
* ``(* 3 4 5 6)`` evaluates to 360
* ``(/ 168 3 8 2)`` evaluates to 3.5
    
Numbers
=======

You can write numbers in many different ways:
    
* 2 (integer)
* 2.3 (decimal)
* 2.345e02 (scientific notation)
* 0x1af (hexadecimal |---| base 16 integers)
* 017 (octal |---| base 8 integers)
* 2r1001 (binary |---| base 2 integers)

Negative numbers start with a `-` as the first character.

Octal doesn’t have an identifying letter like hexadecimal, so if you try to write a number like 009, ClojureScript will complain.
The last form lets you specify the number base |---| 2 in the example |---| followed by the letter `r`, followed by the number.
You can explicitly specify an octal integer as 8r017.

Binding Symbols and Values
==========================

You bind a value and a symbol with ``def``; the general form is

.. parsed-literal::

    (def *symbol* *value*)

Symbols consist of letters, digits, and any of \*, +, !, -, _, ', and  ? |---| but they cannot begin with a numeric. The value may be an expression and may use
previously bound symbols:

::
    
    (def seconds-per-min 60)
    (def min-per-hour 60)
    (def seconds-per-hour (* seconds-per-min min-per-hour))
    
Defining Functions
==================

You define functions with ``defn``. The general form for defining a function is:
    
.. parsed-literal::
    
    (defn *function-name* [*parameter1* *parameter2* ...]
      (*expression*))
    
You can create local bindings within a function with the ``let`` construct:
    
.. parsed-literal::
    
    (defn *function-name* [*parameter1* *parameter2* ...]
      (let [*symbol1* *value1*
            *symbol2* *value2*
            ...]
        (*expression*))
      
The value of the last expression in the function is the value that the function yields.
