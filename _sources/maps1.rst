.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Maps (part 1)
::::::::::::::::::::::::::::::::::::::::::::::
    
We have already covered two of the :doc:`collections </collections.rst>` used in ClojureScript: lists and vectors. Now let us consider **maps**. A **map** is a collection that associates keys with values. Let’s say you wanted to write a program to quiz people about the Canadian provinces and their capitals. You could set up two vectors::
  
  (def provinces ["Alberta", "British Columbia", "Manitoba", "New Brunswick",
                  "Newfoundland and Labrador", "Nova Scotia", "Ontario",
                  "Prince Edward Island", "Quebec", "Saskatchewan",
                  "Yukon", "Nunavut", "Northwest Territories"])
  (def capitals ["Edmonton", "Victoria", "Winnipeg", "Fredericton",
                 "St. John’s", "Halifax", "Toronto",
                 "Charlottetown", "Quebec City", "Regina",
                 "Whitehorse", "Iqaluit", "Yellowknife"])
  
There is nothing wrong with this, but it’s inconvenient. If you let a user enter a province, you must first find its position in the ``provinces`` vector and then look up the corresponding entry in the ``capitals`` vector by its index number; thus, if you determined that Nova Scotia was at position 5 in the ``provinces`` vector (positions start at zero), then you could ``(get capitals 5)``.  It would be nice if you could have a collection where the province acted as the index (also called the *key*) and the capital were the *value*. The **map** collection is exactly that. You define a map as key-and-value pairs in braces:

.. activecode:: map_defined
  :language: clojurescript
  :autorun:
  
  (def capital-map {"Alberta" "Edmonton"
                    "British Columbia" "Victoria"
                    "Manitoba" "Winnipeg"
                    "New Brunswick" "Fredericton"
                    "Newfoundland and Labrador" "St. John’s"
                    "Nova Scotia" "Halifax"
                    "Ontario" "Toronto"
                    "Prince Edward Island" "Charlottetown"
                    "Quebec" "Quebec City"
                    "Saskatchewan" "Regina"
                    "Yukon" "Whitehorse"
                    "Nunavut" "Iqaluit"
                    "Northwest Territories" "Yellowknife"})
Now let’s see what it evaluates to:
  
.. activecode:: print_map
  :language: clojurescript
  :include: map_defined
  
  (println capital-map)
Things to note:
  
* You can put multiple key-and-value pairs on a line, and you can use commas to separate entries; I put each entry on a separate line for readability.
* When you run the code, you will see that the keys and values are all there, but not in the order that they appeared in the source. This is because maps are not inherently ordered.
* Maps appear in many programming languages under different names. If you read about a **hash** (Perl and Ruby), **dictionary** (Python), or an **associative array** (the generic term), that is what ClojureScript and other languages call a map.
  
.. important:: Do not confuse maps, which are a type of collection, with the ``map`` function. That they share a name is unfortunate, but we are stuck with it.

You can put the following examples into the preceding active code to see them at work. To get an entry’s value, you use the ``get`` function. For example, to get Nunavut’s capital, you could say::
  
  (get capital-map "Nunavut")
  
As with lists and vectors, maps are immutable. Any operation on a map leaves the original map untouched. You can use ``conj`` to create a map with a new entry. If Canada were to absorb the fictional country of Latveria as a new province, you could give the new province and capital as a vector::

  (def new-capitals (conj capital-map ["Latveria" "Doomstadt"]))
  
More often, however, you use the ``assoc`` function to create a new map by adding in an arbitrary number of key and value pairs. For example, if Canada were to annex both Ruritania and Graustark, you could say::
  
  (def more-capitals (assoc new-capitals "Ruritania" "Strelsau", "Graustark" "Edelweiss"))
  
If one of the keys in the ``assoc`` arguments already exists in the map, its value will replace the existing value.

You can eliminate key and value pairs from a map by using ``dissoc``, which is followed by a map and the keys you want to remove. The following will get return a new map without the key and value for Latveria and Graustark::
  
  (dissoc more-capitals "Latveria" "Graustark")
  
If you give a key that doesn’t exist in the original map, it will be ignored; it won’t cause an error::
  
  (dissoc more-capitals "Ruritania" "Uqbar") ; gets rid of just Ruritania
  
Iterating through Maps
=========================

You can use both ``map``, ``reduce``, and ``filter`` to process a map.  (Yes, there’s that unfortunate overlap of terms again).  The function that processes each item will receive a vector consisting of the key and value.  Here is an application of ``map`` that will yield a sequence of the province names converted to upper case:
  
.. activecode:: map_map
  :language: clojurescript
  :include: map_defined
  
  (map (fn [item] (.toUpperCase (first item))) capital-map)
  
And here’s some code that uses ``reduce`` to create a new map where the capitals are the key and the provinces are the value. Notice the use of destructuring in the reduction function, which uses the value as key and vice versa:
  
.. activecode:: reduce_map
  :language: clojurescript
  :include: map_defined
  
  (reduce (fn [result [key value]] (assoc result value key))
    {} capital-map)
  
