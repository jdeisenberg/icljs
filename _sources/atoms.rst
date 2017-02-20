.. 

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Atoms
:::::::::::::::

Up to this point, all the data structures we have encountered are **immutable**; when you ``conj`` to a list or a vector, or when you ``assoc`` a value in a map, you end up with a brand new list, vector, or map. This is a good thing. If you pass data to a function, you can do so in complete safety; the function can’t change the value behind your back. 