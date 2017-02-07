:fieldname: orphan

..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

What does Floating Point Mean?
::::::::::::::::::::::::::::::
    
*Floating point* is a term that generally means “a number with a decimal point in it,” as opposed to an integer.
Why is it called such a strange name? It’s not arbitrary; there’s a story behind it.

In some computing languages, you can specify that a value can have a fixed number of decimal places. For example,
monetary amounts will always have exactly two digits to the right of the decimal point; the value of your odometer
has exactly one digit to the right of the decimal point.  Such values are called *fixed point* decimal values.

While fixed point is great for certain applications, this doesn’t work at all for most scientific computing; at some
part of a computation, one decimal place might be enough, but in other parts you might need eight places to get a correct
result. That is, your decimal point can’t be fixed; it has to *float*. Hence the name.

You may also see the term *double* in your travels through computer-land. This is not an arbitrary name either.
This comes from the days when floating point numbers took up four bytes of memory. This is sufficient for 
six to nine decimal places of accuracy. However, scientific computation often needs
better accuracy, so people who designed computer languages allowed you to specify that a floating point number
needed twice the memory |---| eight bytes, or “double precision,” which gives you 15 to 17 digits of precision.
