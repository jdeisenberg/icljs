..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Price and Discount Web Page
:::::::::::::::::::::::::::::

Let’s put together the things you have learned about collections to present a web page where
people can give a list of prices (separated by blanks), and a discount. The page will then show
a bulleted list of the prices after discount:
    
.. raw:: html

   <div style="border: 1px solid gray; padding: 0.25em; margin-top: 0.5em; margin-bottom: 0.5em">
   <p>
   Enter prices, separated by blanks: <input type="text" id="prices" size="35"/>
   </p>
   <p>
   Enter discount: <input type="text" id="discount" size="4"/>%
   </p>
   <p>
   <input type="button" id="calculate" value="Calculate discounted prices"/>
   </p>
   <p>
   Discounted prices:
   </p>
   <div id="result"></div>
   </div>

.. activecode:: price_program
    :language: clojurescript
    :caption: Price Program
    
    ; Your code goes here
    
    
The input elements have ``id`` attribute ``prices`` and ``discounts``, and the output area (currently empty) has an ``id`` attribute ``result``. The calculate button has the ``id`` attribute ``calculate``.

Again, planning is the key here. So let’s think about the tasks you will need to do to transform the
input data to the desired output.
    
* Split the prices into a list of individual strings wherever there is a blank.
* That list needs to be converted to decimal numbers.
* Keep only things that converted successfully; filter out anything that’s not a number.
* Get the discount amount from the input area and convert it to a float.
* Make a new list of the discounted prices
* Format the numbers as money with a currency symbol and two decimal places.
* Surround each of those numbers with  ``<li>`` and ``</li>`` to make them an HTML list item.
* Put them all into one big string between ``<ul>`` and ``</ul>`` to make an HTML bulleted list.
* Make that string the inner HTML of the result area.

Each of these tasks is function-sized; your program might well end up with lots of little functions that get chained together like a conveyor belt in an assembly line. Here are the things you will need to know in JavaScript to accomplish these tasks.

* To split a string ``s`` using blanks as the delimiter, you would say ``(.split s " ")``
* Use the ``js/parseFloat`` to convert a string to a float.
* If a string cannot be converted to float (for example, ``blah``), ``js/parseFloat`` returns the special value ``NaN``, which stands for Not a Number.
* There is a special function ``js/isNaN`` that returns ``true`` if its argument is Not a Number, ``false`` otherwise.
* Let’s say you have a variable ``x`` with the value 123.4567. ``(.toFixed x 2)`` will return the string ``"123.46"``
* Here is a page that tells you :doc:`how to access web page data </web_pages>`

You might be thinking “wow! that’s a *lot* of stuff to handle!”  Yes, this is true. Don’t be discouraged; this is perfectly normal. There is no one part of this program that is particularly hard, but there are a lot of parts to put together. 

You may want to start by writing the sub-parts and testing them one at a time, then link them all together. This is called the “bottom up” approach. Or, you might want to start with the big picture and write the functions as mere placeholders that return a known result. Once that works, you start replacing the subparts with the real functions, one by one. This is called the “top down” approach. You might even want to combine the approaches, writing the subparts and linking them together into the big picture as you go along. I don’t know a formal name for that approach, so let’s call it the “meet in the middle” approach. Whichever approach you use, don’t try to write everything all at once. Write a little, test, and then add more, and test.

You can see my proposed solution on the next page.