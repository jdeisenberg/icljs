..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

De-structuring
''''''''''''''

Back in the :doc:`chapter on reduce </reduce_multi>`, you wrote code to split this series of temperatures::
  
  (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])

into a vector of minimum and maximum temperatures. Here is my solution::
  
  (defn split-temperatures [result item]
    (let [min-temp (first item)
          max-temp (last item)
          min-vec (first result)
          max-vec (last result)]
      (vector (conj min-vec min-temp) (conj max-vec max-temp))))

As you see, there are a lot of clauses in the ``let`` to make the code more readable. You can use ``de-stucturing`` to make the code much more compact without losing readability. The idea of de-structuring (I put in the hyphen so you don’t think I am talking about destruction!) is exactly what the name says: you take a structure apart into its components.  Instead of the two lines for binding ``min-temp`` and ``max-temp`` separately, you can de-structure the ``item`` vector:
  
.. activecode:: destructure_1
  :language: clojurescript
  
  (def temperatures [[3 9] [2 13] [4 10] [4 9] [4 12] [9 20] [16 21]])
  
  (defn split-temperatures [result item]
    (let [[min-temp max-temp] item
          min-vec (first result)
          max-vec (last result)]
      (vector (conj min-vec min-temp) (conj max-vec max-temp))))
    
  (reduce split-temperatures [[][]] temperatures)
  
The destructuring, from now on without a hyphen, is here: ``[min-temp max-temp] item``
The first element in ``item`` is bound to ``min-temp`` and the second element in ``item`` is bound to ``max-temp``.
See if you can modify the preceding code to use destructuring to bind both ``min-vec`` and ``max-vec`` in one go.

You can also destructure in the parameter list. Here is destructuring in the sum and sum of squares example:
  
.. activecode:: destructure_sum_sumsq
  :language: clojurescript

  (defn sum-and-sumsq [[total-sum total-sumsq] value]
      (vector (+ total-sum value)
              (+ total-sumsq (* value value))))

  (reduce sum-and-sumsq [0 0] [1 3 5 2])


The `documentation from clojure.org`_ gives you all the details of destructuring; this page has discussed what they call “sequential destructuring”

.. documentation from clojure.org: https://clojure.org/guides/destructuring

The description and examples there are excellent, and I will not attempt to improve on them or even paraphrase them. I recommend that you copy and paste the examples into the following active code area so you can see them in action.

.. activecode:: try_destructuring
  :language: clojurescript
  
  ; copy and paste code here to try it

  
