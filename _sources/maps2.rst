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
              :name "Annual Talent Show"
              :location {:name "Smith High School"
                         :street "300 Main Street"
                         :city "Anytown"
                         :state "CA"
                         :zip "000000"}
              :contact {:name "Joe Doakes"
                        :email "joe@example.com"
                        :phone "408-555-1234"}})

                         
You can retrieve the state, for example, by doing either of the following.
  
.. activecode:: event_get
  :language: clojurescript
  :include: event_def
  
  (println "Method 1" (get (get event :location) :state))
  (println "Method 2" (:state (:location event)))
  
If you have a deeply-nested structure, though, this can get messy. This is why ClojureScript provides the ``get-in`` function. You give the name of your map followed by a vector of keywords you want to access:
  
.. activecode:: get_in
  :language: clojurescript
  :include: event_def
  
  (get-in event [:location :state])
  
Closely allied with ``get-in`` is ``assoc-in``, which lets you easily create a modified nested map. If there were no ``get-in`` or ``assoc-in``, you would need to do something clunky like this to modify the email (and you have no idea how long it took me to figure it out)::
  
  (assoc event :contact (assoc (:contact event) :email "doakes@example.com"))

It is much easier with ``assoc-in``:
  
.. activecode:: assoc_in
  :language: clojurescript
  :include: event_def
  
  (assoc-in event [:contact :email] "doakes@example.com")
  
If you give a key and value that aren’t in the map, they will be added. So, given the definition of the event, see if you can write an expresson tht will add a ``:price`` key to the event.  The value for that key will be a map with a key ``:adult`` and value 7.50. The resulting map will be::

  {:date "2017-10-02"
   :name "Annual Talent Show"
   :location {:name "Smith High School"
              :street "300 Main Street"
              :city "Anytown"
              :state "CA"
              :zip "00000"}
   :contact {:name "Joe Doakes"
             :email "joe@example.com"
             :phone "408-555-1234"}
   :price {:adult 7.50}}

You don’t have to define the original ``event``.

.. container:: full_width

    .. tabbed:: assoc_exercise

        .. tab:: Your Program

            .. activecode:: assoc_exercise_q
                :language: clojurescript
                :include event_def

                ; your code here

        .. tab:: Answer

            .. activecode:: assoc_exercise_answer
                :language: clojurescript
                :include: event_def

                (assoc-in event [:price :adult] 7.50)

