..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Graphing Program: Lazy Evaluation
''''''''''''''''''''''''''''''''''''

When the program draws the graph, there is one other item that needs to be passed to all the drawing functions: the canvas’s drawing context.  Rather than creating another parameter, this code creates a map that has the context and the conversion function in it. This code summarizes what has been done up to this point and adds the code to set everything up.

.. activecode:: graph_preamble
    :language: clojurescript
    
    (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])

    (defn splitter
      "Split temperatures into vectors of [index min]... and
      [index max]...."
      [data]
      [(into [] (map-indexed
                (fn [index [low hi]]
                [(inc index) hi]) data))
      (into [] (map-indexed
                (fn [index [low hi]]
                [(inc index) low]) data))])

    (defn make-convert
      "Create a function to create graph x-y coordinates
      to screen coordinates in a canvas that is w by h"
      [[min-x max-x] [min-y max-y] w h]
      (let [mx (/ (* 0.85 w) (- max-x min-x))
            my (/ (* 0.85 h) (- min-y max-y))]
        (fn [[x y]]
            [(+ (* mx (- x min-x)) (* 0.075 w))
            (+ (* my (- y max-y)) (* 0.075 h))])))

    (defn make-map
      "Given an x and y range and a canvas ID, create
      a map that has the canvas contet and a function that
      will convert x/y to canvas coordinates."
      [[min-x max-x][min-y max-y] canvasId]
      (let [canvas (.getElementById js/document canvasId)
            w (.-width canvas)
            h (.-height canvas)]
        {:ctx (.getContext canvas "2d")
            :to-screen (make-convert [min-x max-x] [min-y max-y] w h)}))

    (defn find-min-max
      "Return the lowest and highest values from the source data."
      [data]
      (reduce (fn [[acc-min acc-max] [low high]]
        [(if (< low acc-min) low acc-min)
        (if (> high acc-max) high acc-max)]) (first data) (rest data)))

Here is a canvas whose ``id`` is ``graphCanvas``:

.. raw:: html

  <div style="border: 1px solid gray">
  <canvas id="graphCanvas" width="200" height="200">
    This canvas is where the graph will go.
  </canvas>
  </div>

And here is the code to draw the axes as a series of lines that connect points:

.. activecode:: graph_axes
    :language: clojurescript
    :include: graph_preamble


    (defn draw-lines [graph-info points]
        (let [{:keys [ctx to-screen]} graph-info
            [startX startY] (to-screen (first points))]
          (.beginPath ctx)
          (println "Moving to" startX startY)
          (.moveTo ctx startX startY)
          (map (fn [point]
                    (let [[x y] (to-screen point)]
                    (println "Draw to" x y)
                    (.lineTo ctx x y))) (rest points))
          (.stroke ctx)))

    (defn draw-graph [temperatures canvasId]
        (let [[low-coords high-coords] (splitter temperatures)
            [min-temp max-temp] (find-min-max temperatures)
            graph-info (make-map [0 7] [0 max-temp] "graphCanvas")]
            (draw-lines graph-info [[0 max-temp][0 0][7 0]])))

    (draw-graph temperatures "graphCanvas")
    
First, notice that I put ``(println)`` calls in lines 5 and 9 to see what is going on. Second, line 2 uses `associative destructuring <https://clojure.org/guides/destructuring#_associative_destructuring>`_ to extract the context and conversion function from the map. Third, when you run the code |---| the lines don’t appear. What went wrong?

Lazy Evaluation
+++++++++++++++++

What is happening is that the ``map`` function produces results only when some part of the program *needs* that sequence. In every other usage of ``map`` that you have seen before, there has been something to consume the sequence that ``map`` produces. Either it’s output to the screen or part of some other computation. In this case, however, the function that is mapped over has only side effects (creating the canvas path) and doesn’t have any consumer. Nobody needs its results, so it is never called.

This property of lazy evaluation is often quite useful. The ``(range)`` function creates an sequence of numbers; for example, ``(range 5 9)`` creates the sequence ``(5 6 7 8)``.  If you don’t give any numbers, ``(range)`` produces the sequence from 0 to infinity. Let’s say you wanted the first five elements of this infinite sequence. You would write ``(take 5 (range))``. If it weren’t for lazy evaluation, Clojure would have to completely evaluate the ``range`` before doing the ``take``, and evaluating an infinite sequence would take a very long time. Because of lazy evaluation, the ``take`` requires only five elements, so those are the only ones that ``range`` computes.

.. activecode:: lazy_range
    :language: clojurescript
    
    (take 5 (range))

While lazy evaluation can be useful in many cases, it isn’t useful in the graph |---| you *want* the whole sequence computed, whether anyone consumes it or not. If you only have side effects, ``dorun`` will force evaluation of the entire sequence and throw away the results. If you do have results, ``doall`` will force evaluation of the entire sequence and return the result. 

So, to fix the problem with the axes, go to the graphing example, and on line 7, put ``(dorun`` before ``(map``, and add one extra parenthesis at the end of line 10.  Now when you run the program, the ``map`` will be completely evaluated and you will see the axis lines.
