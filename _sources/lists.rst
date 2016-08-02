..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Lists
:::::::::

A list is a series of items inside parentheses. You have been working with lists all throughout this book.  
``(+ 3 5)`` is a list. Its first element is a function, and the remaining elements are numbers. Again, up
until now, every list you have seen has either a function name or a special form as its first element.

But what if you want to create that list of ages from the preceding page? You can’t do this; try it and find out:
    
.. activecode:: bad_list
    :language: clojurescript
    
    (22 43 19 37 28)
  
  
ClojureScript does not let you do this because ``22`` isn’t a function that you can call (hence the error message). So, how
do you get a list that doesn’t have a function as its first element?

* Method 1: use the ``list`` function.  ``(list 22 43 19 37 28)`` produces exactly the desired result, and it follows the rule, because the first item in the parentheses is a function name.
* Method 2: precede the list of items with a single quote ``'``, which tells ClojureScript to interpret what follows literally, without trying to evaluate it. Thus, you could use             ``'(22 43 19 37 28)``

In the case where you have a list of simple values, there is no difference between the methods. However, if you have sub-expressions or symbols, there is a difference, as you can see in this code:
    
.. activecode:: list-differences
    :language: clojurescript
    
    (def x 99)
    (def list1 (list 1 2 (+ 3 4) x 5))
    (def list2 '(1 2 (+ 3 4) x 5))
    (println list1)
    (println list2)
    
The first list, ``list1``, evaluates all of its elements. The second list, ``list2``, takes them literally as given, without evaluation. At this stage, you will probably want the first method. The second method is useful when you are writing *macros*, which, as of this writing, is beyond the scope of this book.

Fundamental Operations
==========================

The following functions, which work on all collections, not just lists, are the very basics:
    
* ``first`` returns the first items in the collection
* ``rest`` returns a sequence of all the items except the first one
* ``last`` returns the last item in the collection
* ``count`` gives you the number of items in the collection
* ``list?`` returns ``true`` if its argument is a list, ``false`` otherwise
* ``conj`` takes a collection and an item, and adds that item to the collection.

In the case of lists, ``conj`` adds the new element at the beginning of the list.  Try these expressions in the following active code box, or use a series
of ``println`` to do them all at once; for your convenience, the ``age-list`` list has been defined.

::
    
    (first age-list)
    (rest age-list)
    (count age-list)
    (list? age-list)
    (conj age-list 55)
    
.. activecode:: try-lists
    :language: clojurescript
    
    (def age-list (list 22 43 19 37 28))

One important aspect of all ClojureScript collections is that they are *persistent*. All the functions that ClojureScript provides to manipulate collections return a new version of the collection.

Again, a concrete example: the ``conj``  function adds a new element to a collection; when used with a list, it adds a new element at the beginning of the list:
    
.. activecode:: list-conj
    :language: clojurescript

    (def age-list (list 22 43 19 37 28))
    (println (conj age-list 27))
    (println age-list)

The first ``println`` adds 27 to the list and prints it, but the original list is untouched, as shown by the second ``println``.