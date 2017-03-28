..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Interacting with JavaScript
''''''''''''''''''''''''''''

Let’s say you wanted to write a function to find the distance between two points (*x*\ :sub:`1`\ , *y*\ :sub:`1`\ )
and (*x*\ :sub:`2`\ , *y*\ :sub:`2`\ ), using the Pythagorean distance formula:

.. raw:: html

    <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
    <semantics>
    <msqrt>
    <mrow>
        <msup>
        <mrow>
        <mo fence="true" stretchy="false">(</mo>
        <mrow>
        <mrow>
            <msub>
            <mi>x</mi>
            <mn>1</mn>
            </msub>
            <mo stretchy="false">−</mo>
            <msub>
            <mi>x</mi>
            <mn>2</mn>
            </msub>
        </mrow>
        </mrow>
        <mo fence="true" stretchy="false">)</mo>
        </mrow>
        <mn>2</mn>
        </msup>
        <mo stretchy="false">+</mo>
        <msup>
        <mrow>
        <mo fence="true" stretchy="false">(</mo>
        <mrow>
        <mrow>
            <msub>
            <mi>y</mi>
            <mn>1</mn>
            </msub>
            <mo stretchy="false">−</mo>
            <msub>
            <mi>y</mi>
            <mn>2</mn>
            </msub>
        </mrow>
        </mrow>
        <mo fence="true" stretchy="false">)</mo>
        </mrow>
        <mn>2</mn>
        </msup>
    </mrow>
    </msqrt>
    <annotation encoding="StarMath 5.0">sqrt{ (x_1-x_2)^2 + (y_1-y_2)^2 }</annotation>
    </semantics>
    </math>
    
       
You will need a square root function, but you can’t write something like ``(sqrt 3)`` because ClojureScript doesn’t have a built-in square root function, you need to use the ``sqrt`` function built into JavaScript’s ``Math`` object. Here’s the code:
    
.. activecode:: distance
    :caption: Distance Formula
    :language: clojurescript
    
    (defn distance [x1 y1 x2 y2]
       (let [xdist (- x1 x2)
             ydist (- y1 y2)]
         (.sqrt js/Math (+ (* xdist xdist) (* ydist ydist)))))
       
    (distance 10 10 15 20)
       
Here’s the key part: ``(.sqrt js/Math ...)``. In order to understand exactly what’s going on, you have to know a little bit about:
    
JavaScript Objects
==================

One of JavaScript’s key concepts is an *object*. You can think of an object as a way of bundling data and the functions related to that data together. (This is a massive, and probably grotesque, oversimplification, but it will serve.)  In object-programming terms, the data are called *properties* and the functions are called *methods*. The ``Math`` object has properties like ``PI`` and methods like ``sqrt``, ``sin``, `and so on`_. A web page has a ``document`` object. One of its properties is the ``title`` property; a piece of data that contains the document’s title. One of a document’s methods is the ``getSelection()`` method; this function returns the text that the person reading the web page has selected. 

.. _and so on: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math

Here are some common tasks you will do with JavaScript objects, and how you do them in ClojureScript. In each instance, you must use ``js/`` to indicate that the object you are manipulating is part of JavaScript (or, to be exact, that the object is in the JavaScript *namespace*).

+------------------------+-----------------------------------------+----------------------------------------------+
| Task                   | ClojureScript                           | Example                                      |
+========================+=========================================+==============================================+
| Call a method          | ``(.method js/object argument ...)``    | ``(.max js/Math 3 5 7 2)``                   |
+------------------------+-----------------------------------------+----------------------------------------------+
| Get a property's value | ``(.-property js/object)``              | ``(.-title js/document)``                    |
+------------------------+-----------------------------------------+----------------------------------------------+
| Create a new object    | ``(js/object.)``                        | ``(js/Date.)``                               |
+------------------------+-----------------------------------------+----------------------------------------------+
| Set a property's value | ``(set! (.-property js/object) value)`` | ``(set! (.-title js/document) "New Title")`` |
+------------------------+-----------------------------------------+----------------------------------------------+

Quick summary: to call a method, precede its name with a dot. To get a property’s value, precede its name with a dot and dash. To create a new object, follow its class name with a dot.

.. activecode:: try-objects
    :language: clojurescript
    
    ; Try the examples.

Exercises
----------
        
.. container:: full_width

    .. tabbed:: radians_q

        .. tab:: Your Program
        
            The trigonometric functions like ``sin`` and ``cos`` require their arguments in `radians`_, but most
            people think of angles in degrees. Write a function named ``to-radians`` that converts its argument
            in degrees to radians. You convert to radians by multiplying by pi and dividing by 180. Use the ``PI``
            property of the ``Math`` object in your solution.

            .. _radians: https://en.wikipedia.org/wiki/Radian

            Then use your ``to-radians`` function to calculate the sine of 30 degrees.
            Because computations have a limited number of digits of accuracy, the result of running
            your code will be something like 0.4999999... instead of exactly 0.5

            .. activecode:: radians_q
                :language: clojurescript
                
                ; your code here

                
        .. tab:: Answer
            
            .. activecode:: radians_answer
                :language: clojurescript
                
                (defn to-radians [degrees]
                    (/ (* degrees (.-PI js/Math)) 180))
                    
                (.sin js/Math (to-radians 30))



.. container:: full_width

    .. tabbed:: interest_q

        .. tab:: Your Program

            Write a function named ``compounding`` that takes four arguments and
            uses this formula for compound interest:
                
            .. raw:: html

                <math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
                <semantics>
                <mrow>
                <mi>P</mi>
                <msup>
                    <mrow>
                    <mo fence="true" stretchy="false">(</mo>
                    <mrow>
                    <mrow>
                    <mn>1</mn>
                    <mo stretchy="false">+</mo>
                    <mfrac>
                        <mi>r</mi>
                        <mi>n</mi>
                    </mfrac>
                    </mrow>
                    </mrow>
                    <mo fence="true" stretchy="false">)</mo>
                    </mrow>
                    <mi mathvariant="italic">nt</mi>
                </msup>
                </mrow>
                <annotation encoding="StarMath 5.0">P( 1 + r over n )^{ nt}</annotation>
                </semantics>
                </math>            

            Where *P* is the principal, *r* is the interest rate, *n* is the number of times
            per year the interest is compounded, and *t* is the number of years you accumulate
            interest.

            To raise a number to a power, use JavaScript ``Math`` object’s ``pow`` function. For example,
            to calculate 3 to the 5th power, you would say ``(.pow js/Math 3 5)``

            Then use your function to calculate the value of a $1,000 principal at an interest rate of
            5% (that is, *r* is 0.05), calculated four times a year for 20 years.

            .. activecode:: interest_q
                :language: clojurescript
                
                (compounding 1000 0.05 4 20)
                
        .. tab:: Answer
            
            .. activecode:: interest_answer
                :language: clojurescript
                
                (defn compounding [principal rate n t]
                    (* principal (.pow js/Math (+ 1 (/ rate n)) (* n t))))
                    
                (compounding 1000 0.05 4 20)


We’ll come back to JavaScript later when we discuss interaction with a web page.
