..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Graphing Program: Closures
'''''''''''''''''''''''''''

All of the functions that do the actual drawing of the graph (axes, lines, dots, etc.), need to convert graph coordinates (*x*, *y*) to the corresponding canvas coordinates, so the program needs a function like ``(to-screen [[x y]])``. But wait |---| this function needs to know the minimum and maximum *x* and *y* as well as the width and height of the canvas. You don’t want to “hard code” the numbers into the function for a particular canvas size (300 x 200) and graph dimensions (*x* from 0 to 7 and *y* from 0 to 25)::

  (defn to-screen [[x y]]
    (let [sx (+ (* (/ (* 0.85 300) 7) x) (* 0.075 300))
          sy (+ (* (/ (* 0.85 200) 25) y) (* 0.075 200))]
      [sx sy]))

That would be good for only this one particular graph, and you might very well want to have more than one graph on a page. On the other hand, you don’t want to have to pass in all that information every time you do a conversion::

  (defn to-screen[[x y] [min-x max-x] [min-y max-y] [w h]]
    (let [sx (+ (* (/ (* 0.85 (- max-x min-x))) (- x min-x)) (* 0.075 w))
          sy (+ (* (/ (* 0.85 (- min-y max-y))) (- y max-y)) (* 0.075 h))]
      [sx sy]))

Surely there must be a better way! `Insert obligatory Airplane joke here.<http://www.vulture.com/2016/01/airplane-dont-call-me-shirley.html>`_ And indeed there is. You write a function that takes all those parameters and returns a conversion function to you. That’s the ``make-convert`` function in the following code:

.. activecode:: make_function
    :language: clojurescript
    
    (defn make-convert [[min-x max-x] [min-y max-y] [w h]]
        (let [mx (/ (* 0.85 w) (- max-x min-x))
              my (/ (* 0.85 h) (- min-y max-y))]
            ;; return anonymous function
            (fn [[x y]]
              [(+ (* mx (- x min-x)) (* 0.075 w))
               (+ (* my (- y max-y)) (* 0.075 h))])))
                
    (def to-screen (make-convert [0 7] [0 25] [300 200]))
    (to-screen [0 0])
    
At this point, you may have an objection: “Hold on a second. The symbols ``mx`` and ``my`` are `local bindings </local_syms.rst>`_  that don’t exist outside of ``make-convert``. Once it finishes returning the anonymous function, dom’t those bindings vanish?”  Ordinarily, this is the case. However, when a function has access to symbols defined outside its scope (in this case, ``mx``, ``min-x``, etc.), those symbols do not vanish. Their values at the time the anonymous function was created are “locked in” to the definition and remain available. In computer science, this is referred to as a **closure** (not to be confused with the Clojure in ClojureScript). To paraphrase Wikipedia, a closure is a record storing a function together with the environment in which it was created.

This solves the problem nicely. You can create a ``to-screen`` function for any size canvas or graph we want and just pass that function as one extra argument to all the drawing functions rather than passing a boatload of arguments at every call.

There is one other item that needs to be passed to all the drawing functions: the canvas’s drawing context.  Rather than creating another parameter, this code creates a map that has the context and the conversion function in it. This code also summarize what has been done up to this point::

    (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])

    (defn splitter
      "Split temperatures into vectors of [index min]... and
      [index max]...."
      [data]
      [(into [] (map-indexed
                (fn [index [low hi]]
                [(inc index) hi] data)))
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
      (reduce (fn [[acc-min acc-max] [low high]])
        [(if (< low acc-min) low acc-min)]
        (if (> high acc-max) high acc-max) (first data) (rest data)))
