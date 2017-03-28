..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Strings
''''''''

All of the functions you have seen so far have worked with numbers or boolean (true/false) values. *Strings* are the other main type of data that you will be transforming with ClojureScript. 

Defining Strings
=================

A string is simply any set of characters between double quotes.
    
::
    
    "This is a string."
    "Multi-language strings: México Россия 日本."
    "Strings can extend
       across multiple lines"

If you need to put a double quote mark inside a string, you must *escape* it by using the backslash character. You also use backslash to include new line characters (``\n``) or tab characters (``\t``) in a string:
    
::
    
    "Please type \"goodbye\" to exit."
    "The \\ character is not often seen alone."
    "Tabs\tspace\tthings\tout."
    "multiple\nlines"
    
Try typing each of these as the definition of ``message`` in the following active code to see how it works.
    
.. activecode:: strings
    :caption: Experiment with strings
    :language: clojurescript
    
    (def message "This is a string.")
    (println message)
    
Combining Strings
==================

The ``str`` function constructs a single string from its arguments. If the argument is not a string, it will be converted to one.

::
    
    (str "cow" "bell") → "cowbell"
    (str "The band has " (* 38 2) " trombones.") → "The band has 76 trombones."
    (str "Is 3 more than 5? " (> 3 5)) → "Is 3 more than 5? false"
    (str 12 34) → "1234"
    (str 56 "78") → "5678"
    
Because ClojureScript compiles to JavaScript, you might be tempted to use the ``+`` function to add strings together. This works, but I advise against it. Leave the plus sign for adding numbers, and use ``str`` for combining strings.

JavaScript String Manipulation
================================

JavaScript has a `whole host of functions for dealing with strings`_, and you call them in exactly the same way that you
:doc:`call any other JavaScript function </js_interact1>` Here are a few of them:

.. _whole host of functions for dealing with strings: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String

* ``(.toUpperCase string)`` returns a new string that is the *string* with letters converted to upper case.
* ``(.indexOf string part)`` returns the position of *part* in *string*; if the *part* isn’t in the *string*, returns -1
* ``(.replace string oldpart newpart)`` returns a new string with *oldpart* replaced by *newpart*
* ``(.startsWith string part)`` returns ``true`` if the string starts with *part*
* ``(.trim string)`` returns a new string with leading and trailing whitespace (blanks, tabs, or new lines) removed
    
Type the preceding function calls (one at a time) in the following activecode area, given the ``def`` that is already there.
    
::
    
    (.toUpperCase message)
    (.replace message "great" "the best")
    (.indexOf message "is")
    (.startsWith message "Clojure")

.. activecode:: strings-js
    :caption: JavaScript String Functions
    :language: clojurescript
    
    (def message "ClojureScript is great!")
    
Converting Strings to Numbers
===============================

As you will see in the section about :doc:`accessing web pages </web_pages>`, when you get information from the person using your program, it will always be in the form of a string. Let’s say your web page asks for a person’s age. When they type ``56``, what you will get is the *string* ``"56"``, and you have to convert it to numeric form.
    
You do this by using JavaScript’s ``parseInt`` function for integers, or with ``parseFloat`` for numbers with decimals.  Here’s how you use such functions:
    
.. activecode:: numeric_conversion
    :caption: Strings to Numbers
    :language: clojurescript
    
    (defn convert-test []
       (let [int-str "123"
             float-str "456.78"
             int-value (js/parseInt int-str)
             float-value (js/parseFloat float-str)]
         (+ int-value float-value)))
       
     (convert-test)
     
.. note::
    
    If you do something like this: ``(js/parseInt "12.95")`` you will get 12 as a result; ``parseInt`` stops as soon as it finds something that couldn’t be part of an integer, so ``(js/parseInt "99Luftballons")`` results in 99.

Clojure String Manipulation
=============================

ClojureScript also lets you use a string manipulation library from its “parent” language Clojure. To use these functions (`detailed here`_), you prefix their names
with ``clojure.string/``. Here are some of the Clojure string functions, many of which are similar to those in the preceding section.

.. _detailed here: http://clojuredocs.org/clojure.string
    
* ``(clojure.string/upper-case string)`` returns a new string that is the *string* with letters converted to upper case.
* ``(clojure.string/replace-first string oldpart newpart)`` returns a new string with first occurrence of *oldpart* replaced by *newpart*
* ``(clojure.string/replace string oldpart newpart)`` returns a new string with all occurrences of *oldpart* replaced by *newpart*

The ``clojure.string`` library doesn’t work in the activecode environment, so this book will stick to the JavaScript string manipulation functions. When you write your own ClojureScript programs, I strongly advise you to use the ``clojure.string`` library instead.

