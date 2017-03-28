..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Experimenting with canvas methods
''''''''''''''''''''''''''''''''''

Here is your canvas (200 x 200):

.. raw:: html

  <div style="border: 1px solid gray">
  <canvas id="drawing2" width="200" height="200">
    This canvas is for your experimenting pleasure.
  </canvas>
  </div>

Here is code to get the context and, for your convenience, a function to clear the canvas. Add any code you want to experiment further.

.. activecode:: canvas_experiment
  :language: clojurescript

  (def canvas (.getElementById js/document "drawing2"))
  (def ctx (.getContext canvas "2d"))
  
  (defn clear-canvas []
    (let [w (.-width canvas)
          h (.-height canvas)]
      (.beginPath ctx)
      (set! (.-fillStyle ctx) "white")
      (.rect ctx 0 0  w h)
      (.fill ctx)))
      
Here are some of the things you can put in a path. A complete summary is `at this link <https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D#Paths>`_

``(.beginPath ctx)``
    Begins a new subpath
  
``(.closePath ctx)``
    Draws a line from current position to starting position of subpath. If the path is already closed, this has no effect.
  
``(.moveTo ctx x y)``
    Moves current position to given (*x*, *y*) coordinate
  
``(.lineTo ctx x y)``
    Draw a line from current position to given (*x*, *y*) coordinate
  
``(.arc ctx cx cy r startθ endθ ccw)``
    Draw an arc with center at (*cx*, *cy*) and radius *r*. The start angle and end angle (*startθ* and *endθ*) are given in radians. If *ccw* is ``true``, the arc is drawn counterclockwise (the default is clockwise).
  
``(.arcto ctx x1 y1 x2 y2 r)``
    Draw an arc from point (*x1*, *y1*) to point (*x2*, *y2*). The arc is part of a circle with radius *r*.
