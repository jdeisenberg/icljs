..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Collections
''''''''''''

So far, we have been working with symbols bound to a single variable, as in ``(def price 3.95)``. But what if you had a group of
five prices that you wanted to work with, for example, discounting them all by 10% or finding their mean and standard deviation? You certainly don’t want to do something like this:
    
::

    (def price1 3.95)
    (def price2 6.80)
    (def price3 2.49)
    (def price4 5.33)
    (def price5 1.99)
    
Imagine what would happen if you had twenty prices to keep track of. There must be a better way, and that better way is
*collections*, which allow you to bind a single symbol to a collection of related data. 

The main types of collections in Clojurescript are:
    
* **list**: a sequence of items, usually intended to be processed sequentially from beginning to end. Thus:
    
  ``(def price-list (list 3.95 6.80 2.49 5.33 1.99))``
  
* **vector**: a sequence of items, intended to be accessed by their position (index)

  ``(def price-vector [3.95 6.80 2.49 5.33 1.99])``
  
* **map**: a collection that lets you associate unique keys with values, intended to be accessed by key; in other programming languages this is aptly called a “dictionary.” In a dictionary, a word (the key) is associated with its definition (a value), and you look things up by word. Unlike a dictionary, the keys of a map are not stored in any particular order. When writing a map definition, you give key/value pairs inside braces. The comma between the pairs is not necessary, but it is added here for clarity of reading.

  ``(def price-map {"notebook" 3.95, "markers" 6.80, "staples" 2.49, "crayons" 5.33, "erasers" 1.99})``
  
* **set**: a collection containing unique elements. You put the elements in braces that are preceded by a hashmark ``#``\ .

  ``(def price-set #{3.95 6.80 2.49 5.33 1.99})``
  
