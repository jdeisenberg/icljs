..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Graphing Program: Solution
''''''''''''''''''''''''''''''''''''

Here is my solution. You can :download:`download a .ZIP file version of the project here. <zipfiles/graphing.zip>`.

.. raw:: html

  <div style="border: 1px solid gray">
  <canvas id="graphCanvas" width="200" height="200">
    This canvas is where the graph will go.
  </canvas>
  </div>


.. activecode:: graph_solution
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
      [graph-info points]
      (let [{:keys [ctx to-screen]} graph-info]
        (dorun (map (fn [point]
                     (let [[x y] (to-screen point)]
                      (.beginPath ctx)
                      (.arc ctx x y 3 0 (* 2 (.-PI js/Math)) 0)
                      (.fill ctx)))
                    points))))
  
    (defn xlabel
      "Draw tick marks and labels for x-axis
      from minimum to maximum value with step as interval"
      [graph-info min max step]
      (let [{:keys [ctx to-screen]} graph-info]
        (doall
          (map (fn [x]
                (let [[sx sy] (to-screen [x 0])
                      w (.-width (.measureText ctx (str x)))]
                 (.beginPath ctx)
                 (.moveTo ctx sx (+ sy 3))
                 (.lineTo ctx sx (- sy 3))
                 (.stroke ctx)
                 (.fillText ctx (str x) (- sx (/ w 2)) (+ sy 12))))
            (range min (+ max step) step)))))
  
    (defn ylabel
      "Draw tick marks and labels for y-axis
      from minimum to maximum value with step as interval"
      [graph-info min max step]
      (let [{:keys [ctx to-screen]} graph-info]
        (doall
          (map (fn [y]
                (let [[sx sy] (to-screen [0 y])
                      ystr (str y)
                      w (.-width (.measureText ctx ystr))]
  
                 (.beginPath ctx)
                 (.moveTo ctx (+ sx 3) sy)
                 (.lineTo ctx (- sx 3) sy)
                 (.stroke ctx)
                 (.fillText ctx ystr (- sx (+ 5 w)) (+ sy 4))))
            (range min (+ max step) step)))))
  
  
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
       
    (draw-graph temperatures "graphCanvas")
  
