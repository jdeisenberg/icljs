.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Maps (part 2)
::::::::::::::::::::::::::::::::::::::::::::::
    
The `preceding page </maps1.rst>`_ shows string keys mapped to some other type of value. This is a typical use of maps in most programming languages. In ClojureScript, maps are also used to create **data structures**. Instead of using strings as keys, they use **keywords**. A keyword is a symbol name preceded by a colon, and they are widely used in ClojureScript.

Let’s say you wanted to a data structure to describe a Canadian province that would show the province name, its capital, its population, and its latitude and longitude (as a vector of two numbers). You could set up a map like this for Ontario:
  
.. activecode:: map_data_structure
  :language: clojurescript
  :autorun:
  
  (def province {:name "Ontario"
                 :capital "Toronto"
                 :population 2731571
                 :coordinates [43.7 -79.4]})
  
You can use ``get`` to access any part of the data:
  
.. activecode:: map_get
  :language: clojurescript
  :include: map_data_structure
  
  (get province :population)
  
If you use keywords as your map’s keys, you can also use the keys as if they were a function name. Here is the equivalent of the preceding example:
  
.. activecode:: keyword_as_function
  :language: clojurescript
  :include: map_data_structure
  
  (:population province)

And, if the population changes, you can use ``assoc`` to create a new map with an updated part of the data structure:
  
.. activecode:: update_map
  :language: clojurescript
  :include: map_data_structure
  
  (assoc province :population 2800000)
  
You can have maps within maps. Consider this data structure for an event:
  
.. activecode:: event_def
  :language: clojurescript
  :autorun:
    
  (def event {:date "2017-10-02"
              :name "My Fair Lady"
              :location {:name "Smith High School"
                         :street "300 Broadway"
                         :city "Anytown"
                         :state "CA"
                         :zip "000000"}
              :contact {:name "Joe Doakes"
                        :email "joe@example.com"
                        :phone "408-555-1234"}})

                         


