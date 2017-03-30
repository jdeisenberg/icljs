..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Graphing Program: Completion
''''''''''''''''''''''''''''''''''''

You now know nearly everything you need to complete the project: you can draw the tick marks on the axes and you can draw the dots on the graph using the ``.arc`` method. When it comes to labeling the axes, you do not want the text to overwrite the tick marks, so you need to know how much room the text takes up.

The code to find out how wide some text is looks like this, where ``ctx`` is the graphic context::

  (.-width (.measureText ctx "Some text"))
  
For details see, the Mozilla documentation about the ``measureText`` method (`link <https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/measureText>`_\ ) and the ``textMetrics`` object (`link <https://developer.mozilla.org/en-US/docs/Web/API/TextMetrics>`_\ ).

At this point you might also want to create a ClojureScript project as described in `Appendix C </appendix_c.rst>` to complete the project rather than working in the browser. (You’ll eventually be creating ClojureScript projects, so why not start now?) If you do this, here is the HTML that you will need to put in the ``resources/public_html/index.html`` file::

    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div id="app">
        <h2>Graphing Example</h2>
        <canvas id="graphCanvas" width="250" height="250"
            style="border: 1px solid gray"></canvas>
        </div>
        <script src="js/compiled/graphing.js" type="text/javascript"></script>
    </body>
    </html>

Here is the canvas:

.. raw:: html

  <div style="border: 1px solid gray">
  <canvas id="graphCanvas" width="200" height="200">
    This canvas is where the graph will go.
  </canvas>
  </div>

Here is the code that has been presented so far, plus some utility functions that I found helpful in creating the solution, plus **stubs** (placeholders) for the remaining functions. Feel free to fill in those stubs, or erase everything and write your own (better, improved) version.

.. activecode:: graph_with_stubs
    :language: clojurescript
    
    (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])
  
    ;
    ; The following four functions are utility functions
    ; to make other code easier
    ;
    (defn setcolor
      "Utility routine: set stroke and fill color for current context"
      [graph-info color]
      (let [ctx (:ctx graph-info)]
       (set! (.-strokeStyle ctx) color)
       (set! (.-fillStyle ctx) color)))
  
    (defn lower-multiple
         "Find closest lower multiple of n, with m as multiplier;
         (lower-multiple 7 2) -> 6"
         [n m]
         (* m (quot n m)))
  
    (defn higher-multiple
      "Find closest higher multiple of n with m as multiplier;
      (higher-multiple 7 2) -> 8"
      [n m]
      (* m (quot (+ n (dec m)) m)))
  
    (defn clear-canvas
      "Erase canvas; uses clearRect and canvas methods"
      [graph-info]
      (let [ctx (:ctx graph-info)
            canvas (.-canvas ctx)] ; get parent canvas
       (.clearRect ctx 0 0 (.-width canvas) (.-height canvas))))
  
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
  
    (defn draw-lines
      "Draw a series of connected lines given a vector of points"
      [graph-info points]
      (let [{:keys [ctx to-screen]} graph-info
            [startX startY] (to-screen (first points))]
        (.beginPath ctx)
        (.moveTo ctx startX startY)
        (dorun (map (fn [point]
                     (let [[x y] (to-screen point)]
                      (.lineTo ctx x y))) (rest points)))
        (.stroke ctx)))
  
    (defn draw-dots
      "Draw a series of dots of radius 3 at the given points"
      [graph-info points])
  
    (defn xlabel
      "Draw tick marks and labels for x-axis
      from minimum to maximum value with step as interval"
      [graph-info min max step])
  
    (defn ylabel
      "Draw tick marks and labels for y-axis
      from minimum to maximum value with step as interval"
      [graph-info min max step])
  
  
    (defn draw-graph [temperatures canvasId]
      (let [[low-coords high-coords] (splitter temperatures)
            [min-temp max-temp] (find-min-max temperatures)
            graph-info (make-map [0 7] [0 max-temp] "graphCanvas")]
          (clear-canvas graph-info)
       (setcolor graph-info "black")
       (draw-lines graph-info [[0 max-temp][0 0][7 0]]) ; axes
       (set! (.-font (:ctx graph-info)) "9px sans-serif")
       (xlabel graph-info 1 7 1)
       (ylabel graph-info (lower-multiple min-temp 5)
        (higher-multiple max-temp 5) 5)
        
       (setcolor graph-info "blue")
       (draw-lines graph-info low-coords)
       (draw-dots graph-info low-coords)
  
       (setcolor graph-info "red")
       (draw-lines graph-info high-coords)
       (draw-dots graph-info high-coords)))

