..  Copyright © J David Eisenberg

Exercises in Arithmetic
''''''''''''''''''''''''

.. container:: full_width

    1.

        .. tabbed:: q1

            .. tab:: Question

                Convert these infix expressions to the corresponding ClojureScript expressions.
                The number after the arrow is the value you should get as a result. You can use
                the active code box to test your expressions.

                #. ``5 * 2`` → 10
                #. ``3 + 4 * 7 - 5`` → 26
                #. ``(3 + 6) * (9 - 5)`` → 36
                #. ``12 / 15 * 4`` → 3.2
                #. ``4 * (12 * 3) / (13 + 35)`` → 3 
                #. ``((9 - 12) / 5) * 7`` → -4.2
                #. ``((8 - 10) * 11) - ((14 - 2) + 7)`` → -41

                .. activecode:: arithmetic_exercises_questoin
                   :language: clojurescript

                   (* 5 2)

            .. tab:: Answer

                #. ``(* 5 2)`` → 10
                #. ``(+ 3 (- (* 4 7) 5))`` → 26
                #. ``(* (+ 3 6) (- 9 5)`` → 36
                #. ``(* (/ 12 15) 4)`` → 3.2
                #. ``(* 4 (/ (* 3 12) (+ 13 35)))`` → 3
                #. ``(* (/ (- 9 12) 5) 7)`` → -4.2
                #. ``(- (* (- 8 10) 11) (+ (- 14 2) 7))`` → -41

                .. activecode:: arithmetic_exercises_answer
                   :language: clojurescript
