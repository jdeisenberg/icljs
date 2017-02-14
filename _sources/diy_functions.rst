..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Writing Your Own Functions
::::::::::::::::::::::::::

These built-in functions (and ClojureScript has many, many more) are all well and good, but I’m guessing you are wondering how you can write your own functions. Wonder no longer; here we go.

The Parts of a Function
========================

Let’s start with implementing an ``average`` function that takes two arguments and yields their average as a result. Here’s the definition:
    
::

    (def average (fn [a b]
        (/ (+ a b) 2.0)))

Analyzing this step by step:
    
* ``def average`` says that you want to bind the symbol ``average`` to some value.
* That value is the special form ``(fn ...)``, which means “function”.
* The first argument to ``fn`` is a *vector* of parameter names. A vector is a sequence of items in square brackets. (You will learn more about vectors in :doc:`an upcoming chapter <vectors>`.) The function you’re defining needs two inputs, so there are two items in the vector. In this case, they have generic names: ``a`` and ``b``.
* The second argument to ``fn`` is the *function body.* In this case, it consists of one nested expression: ``(/ (+ a b) 2.0)``. The value of the last expression in the function body is the function’s result.

Once a function is defined, you can call it exactly like any other ClojureScript function; you give its name after an opening parenthesis, follow it by the arguments you want to transform, and close the parentheses.

.. activecode:: average_function
    :caption: The average function
    :language: clojurescript
    
    (def average (fn [a b]
        (/ (+ a b) 2.0)))
    
    (average 5 17)

.. reveal:: reveal_params
    :showtitle: Show: What are parameters and arguments?
    :hidetitle: Hide

    You can think of a *parameter* as a placeholder; it’s “extra information” that a function needs to do its job. For example, if I asked you to “calculate the square root,” you would ask me, “The square root *of what*?”  That “what” is a parameter.
    
    When you call the function, you have to provide a value to bind to that placeholder; you have to provide the number whose square root you want. That value is the *argument* to the function.
    
    A **p**\arameter is a **p**\laceholder symbol in the defintion of the function.
    
    An **a**\rgument is the **a**\ctual value that will bind to the placeholder.
                                                                                
    So, in the preceding example, ``a`` and ``b`` are the parameters; when you make the function call, the ``5`` and ``17`` are the arguments whose values will be bound to the parameters.
    
Here’s another function with two parameters; it finds the area of an ellipse as shown in the following figure, using the formula π ∙ a ∙ b:
    
.. figure:: images/ellipse.png
    :alt: Ellipse with labels for semi-major axis a and semi-minor axis b
    
    Ellipse with semi-major and semi-minor axis
    
.. activecode:: ellipse_area
    :caption: Calculate area of ellipse
    :language: clojurescript
    
    (def ellipse-area (fn [a b]
        (* 3.14159265 a b)))
    
    (ellipse-area 3 7)
    
Now, you try it. Write a function named ``surface-area`` that calculates the surface area of a rectangular prism with sides of length *a*, *b*, and *c*. The formula is 2(*ab* + *bc* + *ac*).

.. figure:: images/prism.png
    :alt: Rectangular prism with length, height, and width labeled a, b, and c
    
    Rectangular prism

.. container:: full_width

    .. tabbed:: rect_q

        .. tab:: Your Program
        
            .. activecode:: prism
                :language: clojurescript
                
                ; your code here
                
                (surface-area 3 5 7) ; answer should be 142
                
        .. tab:: Answer
            
            .. activecode:: prism_answer
                :language: clojurescript
                
                (def surface-area (fn [a b c]
                    (* 2 (+ (* a b) (* b c) (* a c)))))
                    
                (surface-area 3 5 7)


A Shortcut for Defining Functions
=================================

Defining functions is such a common operation in ClojureScript that the language provides a shortcut: ``defn``, which combines ``def`` and ``fn``.
In short, you use ``defn`` instead of ``def`` and drop the opening ``(fn`` and its closing ``)``. As a result, the parameter vector immediately follows the function name.
As a concrete example, here are the definitions of ``average`` and ``ellipse-area`` in the shortcut form:
    
.. activecode:: defn
    :caption: Using defn to define functions
    :language: clojurescript
    
    (defn average [a b]
      (/ (+ a b) 2.0))
    
    (defn ellipse-area [a b]
      (* 3.14159265 a b))
    
    (println (average 5 17))
    (println (ellipse-area 5 3))

This book will use the ``defn`` special form for most of its function definitions because it is so convenient. If you are a fan of ``fn``, do not be disappointed; it will make its triumphant return when we discuss :ref:`anonymous functions <anonymous-functions>`.
