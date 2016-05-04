..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Strings
::::::::::::::::

All of the functions you have seen so far have worked with numbers or boolean (true/false) values. *Strings* are the other main type of data that you will be transforming with ClojureScript. 

Defining Strings
=================

A string is simply any set of characters between double quotes.
    
::
    "This is a string."
    "Multi-language strings: México Россия 日本."
    "Strings can extend
       across multiple lines"

If you need to put a quote mark inside a string, you must *escape* it by using the backslash character. You also use backslash to include new line characters (``\n``) or tab characters (``\t``) in a string:
    
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
    message
    

