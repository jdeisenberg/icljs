..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Graphing Program: Outline
'''''''''''''''''''''''''''

As a reminder, the object is to transform this data::

    [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]]
    
into this graph:

.. image:: images/temperature_graph.png
    :alt: Line graph showing max temperature as red line and min temperature as blue line

The program will have to:

* Split the temperatures into two sets of *x*, *y* pairs to be graphed::

    [[[1 3] [2 2] [3 4] [4 4] [5 4] [6 9] [7 16]]
    [[1 9] [2 13] [3 10] [4 9] [5 12] [6 20] [7 21]]]
    
* Draw the axes:

  * Draw the lines
  * Draw the tick marks
  * Draw the labels
    
* Draw a connected line for the minimum teperatures
* Draw dots for the minimum temperatures
* Draw a connected line for the maximum temperatures
* Draw dots for the maximum temperatures

Before moving on to all the drawing, let’s do the splitting. The trick here is to use the ``map-indexed`` function. It works like ``map``, except that the function you provide has two parameters: the “index number” and the item from the collection being mapped. Here is an example that takes a list of words and returns a vector of upper-cased words and their position in the list (starting at zero):

.. activecode:: map_indexed_example
    :language: clojurescript

    (defn counted-upper [index item]
      (vector index (.toUpperCase item)))
      
    (map-indexed counted-upper ["Cat" "DoG" "birD"])
    
Now, see if you can do the split of the temperatures. Hint: use ``map-indexed`` twice. The first time, extract the first item in the temperature pair (the low temperature). The second time, extract the second item in the temperature pair. Remember that the index stars at zero, so you will want to add one; you can use the ``inc`` function for that.

.. container:: full_width

        .. tabbed:: q1

            .. tab:: Question

                .. activecode:: split_indexed_question
                   :language: clojurescript

                   (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])
                   
                   (defn splitter[data]
                     ; your code here
                     )
                     
                   (splitter temperatures)

            .. tab:: Answer

                .. activecode:: split_indexed_answer
                   :language: clojurescript
                   
                   (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])
                   
                   (defn index-min [index temperature-pair]
                     [(inc index) (first temperature-pair)])
                        
                   (defn index-max [index temperature-pair]
                     [(inc index) (last temperature-pair)])
                        
                   (defn splitter [data]
                     [(into [] (map-indexed index-min data))
                      (into [] (map-indexed index-max data))])
                        
                   (splitter temperatures)


