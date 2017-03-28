..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Atoms
''''''

Up to this point, all the data structures we have encountered are **immutable**; when you ``conj`` to a list or a vector, or when you ``assoc`` a value in a map, you end up with a brand new list, vector, or map. This is a good thing. If you pass data to a function, you can do so in complete safety; the function can’t change the value behind your back. (This is especially valuable when using functions written by other people.)

Sometimes, though, you need to have data that is mutable either for convenience or out of necessity. For example, if you have a game where you have a player’s score, it changes depending upon actions that may take place in many different functions.  Here is how you might create this atom:
  
.. activecode:: def_atom
  :language: clojurescript
  
  (def score (atom 0))
  
Now, let’s see what happens when you print the value:
  
.. activecode:: print_atom
  :language: clojurescript
  :include: def_atom
  
  (println score)
  
There’s a surprise! An atom seems to contain more information than just the number. An atom is really a data type that contains a **reference** to the value, so to get the value of an atom, you must *deference* it, in one of two ways:
  
.. activecode:: deref_atom
  :language: clojurescript
  :include: def_atom
  
  (println (deref score))
  (println @score)
  
If a function wants to change the score, it uses the ``swap!`` function.  The ``!`` at the end of the function name is a ClojureScript convention to tell you that the function changes its argument.  The ``swap!`` is followed by the name of the atom, then a function and arguments to apply to the argument. So, if you wanted to add one to the score, you could do this:
  
.. activecode:: swap_atom
  :language: clojurescript
  :include: def_atom
  
  (swap! score + 1)
  (println @score)
  
The value of ``swap!`` is the updated atom; if you get rid of the ``println`` in the preceding active code, you will still see the 1 as the return value.

If, at some point, you had to reset the score to zero, you could do it with ``reset!`` followed by the atom name and the new value::
  
  (reset! score 0)
  
The ``reset!`` function returns the new value; in this case, zero.

Maps as Atom Values
========================

To extend the preceding example, let’s say you needed to keep track of the player’s name, score, and number of lives. You could create three separate atoms, but it is more convenient (and more idiomatic ClojureScript) to make a single atom that refers to a map:
  
.. activecode:: define_player
  :language: clojurescript
  
  (def player (atom {:name "Dread Pirate Roberts",
                     :score 0,
                     :lives 10
                     :health 100}))
  
If you want to increase the player’s score by 5, you use code like this:
  
.. activecode:: modify_score
  :language: clojurescript
  :include: define_player
  
  (swap! player update :score + 5)
  
.. note::
  
  This page needs some sort of wrap-up exercise, but it escapes me at the moment.
  
