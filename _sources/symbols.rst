..  Copyright © J David Eisenberg and O'Reilly Media
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Symbols
:::::::::

Doing arithmetic with concrete numbers is fine, but when you move from arithmetic to algebra, you use variables so that you can manipulate abstract symbols. Similarly, in ClojureScript, you want to be able to describe transformations of data in abstract terms.  Before we talk about ClojureScript, let’s look a bit more closely at algebraic variables.

In algebra, when you say something like

    *x* = 5
    
that means that you are using the symbol *x* to represent 5. Wherever you have a 5, you can substitute *x*; wherever you have an *x*, you can substitute 5.  Similarly, when you say:
    
    *y* = *x* + 3
    
That means the symbol *y* represents the quantity *x* + 3, and you can substitute one for the other. 

Another feature of algebraic symbols is that, once you set them, you can’t change your mind. You can’t be halfway through a calculation and all of a sudden claim that:
    
    *x* = 6
    
because you said that *x* symbolizes 5, and five certainly does not equal six!


Symbols in ClojureScript
========================

Symbols in ClojureScript work much like algebraic values. You use the ``def`` function to **bind** a symbol to a value. 
The ``def`` function takes two arguments: the symbol and the value. Once a symbol is bound,
you can use it in expressions, including definitions of other symbols.

.. activecode:: symbol_def
    :caption: Define Symbol Bindings Here
    :language: clojurescript
    
    (def years 62)
    (def days (* 365 years))
    days

.. reveal:: nonprogrammer_sym
    :showtitle: Click to read this if you have not programmed before
    :hidetitle: Hide
    
    In many other programming languages, symbols are called *variables*, and they are not bound to values as in ClojureScript.
    Instead, a variable is a name for a location in memory; when you say ``x = 5``, that puts 5 into the memory location labeled ``x``.
    This operation is called *assigning* to a variable rather than *binding* to a symbol, and it doesn’t work like algebra at all.
    In these other languages, it’s perfectly valid to say ``x = 6`` and put a new value into the same memory location. In this book, I will use the words
    “symbol” and “bind” to help you keep ClojureScript’s algebra-like model in mind rather than the model used by other languages.

.. reveal:: programmer_sym
    :showtitle: Click to read this if you have programmed before
    :hidetitle: Hide

    You are probably used to a statement like ``x = 5`` being called an *assignment statement* that means
    “put 5 into a memory location that has been labeled ``x``,” and ``x`` is called a *variable* rather than a symbol.
    One of the larger hurdles in learning a language like ClojureScript is understanding that its symbols (variables)
    work more like variables in algebra than like labeled memory locations.
    That’s why I am using the words “symbol” and “bind” in this book rather than “variable” and “assign,” to help you
    get used to this different mental model.

.. note::

    Unlike true algebraic symbols, it is possible to re-bind a new value to a symbol in ClojureScript, but you don’t need to do it often.
    Normally you will consider a binding to be *immutable* |---| once bound, you never change a symbol’s value.

What’s in a (Symbol) Name?
===============================

Symbols must start with a non-numeric character, followed by letters, digits, or any of \*, +, !, -, _, ', and  ?.

Making your symbol names meaningful is an important part of programming.  If, instead of using ``years`` I had used ``y``, the code wouldn’t be as clear; ``y`` could also refer to a graphical *y*-coordinate.

Sometimes you might have a symbol that is best described by two words, such as an interest rate. Just calling it ``rate`` is not good; a financial program could have interest rates, penalty rates, or any number of types of rates. You can’t call it ``interest rate`` because you can’t put spaces in a symbol name. There are three ways that people solve the problem of writing multi-word names:
    
* ``interestRate`` This is called *camel case*, where every word after the first begins with a capital letter (it’s called camel case because the capital letters are distantly reminiscent of a camel’s humps).
* ``interest_rate`` In this method, words are separated by underscores.
* ``interest-rate`` Words are separated by hyphens. This is what you will see most often in ClojureScript.

Again, in terms of meaningfulness, a name like ``ir`` would be far too short, and ``interest-rate-calculated-on-a-per-month-basis`` would be ridiculously long.

.. reveal:: symbol_reveal_1
    :showtitle: See extra info
    :hidetitle: Hide extra info

    ClojureScript’s rules for symbols give you a great deal of power.
    You can abuse that power by writing confusing code like this:
        
    .. activecode:: symbol_def2
        :caption: How to Ruin Your Life
        :language: clojurescript
        
        (def def 2)
        (def + 3)
        (def - 4)
        (* def (/ + -))

    Or you can use that power wisely. For example, by “letter,” ClojureScript doesn’t just mean A through Z;
    you can use alphabetic characters in any language. Here’s
    the first example with the names in Russian:

    .. activecode:: symbol_def3
        :caption: Letters aren’t just A-Z
        :language: clojurescript
        
        (def лет 62)
        (def дней (* лет 365))
        дней
        

You Try It
----------

Give this a try: define a symbol named ``hours`` and another named ``minutes``. Bind them to any values you like. Then define a third symbol named ``total-minutes`` that is bound to 60 times ``hours``, plus ``minutes``.

.. tabbed:: symbol_tabs

    .. tab:: Try it
    
        .. activecode:: symbol_def3_question
            :above
            :language: clojurescript

            ; Your code here

    .. tab:: Answer

        .. activecode:: symbol_def3_answer
            :above
            :language: clojurescript
            
            (def hours 3)
            (def minutes 54)
            (def total-minutes (+ (* hours 60) minutes))
            total-minutes
