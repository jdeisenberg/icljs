..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Collections
:::::::::::::::

So far, we have been working with symbols bound to a single variable, as in ``(def age 22)``. But what if you had a group of
five ages, whose mean and standard deviation you wanted? You certainly don’t want to do something like this:
    
::
    
    (def age1 22)
    (def age2 43)
    (def age3 19)
    (def age4 37)
    (def age5 28)
    
Imagine what would happen if you had twenty people to keep track of. There must be a better way, and that better way is
*collections*, which allow you to bind a single symbol to a collection of related data. 

The main types of collections in Clojurescript are:
    
* **list**: a sequence of items, usually intended to be processed sequentially from beginning to end. Thus:
    
  ``(def age-list (list 22 43 19 37 28))``
  
* **vector**: a sequence of items, intended to be accessed by their position (index)

  ``(def age-vector [22 43 19 37 28])``
  
* **map**: a collection that lets you associate unique keys with values, intended to be accessed by key; in other programming languages this is aptly called a “dictionary.” In a dictionary, a word (the key) is associated with its definition (a value), and you look things up by word.

  ``(def age-map {"Nancy" 22, "Fernando"  43, "Loc" 19, "Jeanne" 37, "Joe" 28})``
  
* **set**: a collection containing unique elements

  ``(def age-set #{22 43 19 37 28})``
  
One important aspect of all ClojureScript collections is that they are *persistent*. All the functions that ClojureScript provides to manipulate collections return a new version of the collection.

Again, a concrete example: the ``conj``  function adds a new element to a collection; when used with a list, it adds a new element at the beginning of the list:
    
.. activecode:: list-conj
    :language: clojurescript

    (def age-list (list 22 43 19 37 28))
    (println (conj age-list 27))
    (println age-list)

The first ``println`` adds 27 to the list and prints it, but the original list is untouched, as shown by the second ``println``.