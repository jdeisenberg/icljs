..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Accessing Web Pages
''''''''''''''''''''

Up to this point, your interaction with JavaScript has only been making calls to its functions. You may also have noticed that all the input for the functions have come from arguments that you have entered in ClojureScript. Modifying a previous example:
    
.. activecode:: symbol_def
    :caption: Input in Code
    :language: clojurescript
    
    (defn age-in-days [years]
      (* years 365))
    
    (age-in-days 63)
    
That works for me at my present age, but you probably aren’t 63 years old, and even if you are, next year both you and I will be older, so we will have to change the argument to ``age-in-days``. That’s OK for us; we’re programmers and we are cool with that :) We can’t, however, expect people using our programs to go rooting around in our code to get the results they want.
    
For people who are used to web pages, you want to write HTML like this:
    
::
    
   <p>
   Enter your age in years:
       <input type="text" id="years" />
       <input type="button" id="calculate"
         value="Calculate age in days"/>
   </p>
   <p id="result"></p>
   
...that looks like this:
    
.. raw:: html

   <div style="border: 1px solid gray; padding: 0.25em; margin-top: 0.5em; margin-bottom: 0.5em">
   <p>
   Enter your age in years:
       <input type="text" id="years" />
       <input type="button" id="calculate"
         value="Calculate age in days"/>
   </p>
   <p id="result"></p>
   </div>
    
   
...where they can enter their age in years, click a button, and see a result. The code to handle this has to do the following:

* Read the input area
* Calculate the desired number
* Place a message in the result paragraph

That code has to be activated whenever the button gets clicked. Here is code that does exactly that:
 
.. activecode:: interact
    :language: clojurescript
    :autorun:
    :caption: Simple interaction
    
    (def input-element (.getElementById js/document "years"))
    (def button-element (.getElementById js/document "calculate"))
    (def result-element (.getElementById js/document "result"))
    
    (defn calculate [evt]
      (let [years (js/parseInt (.-value input-element))
            days (* 365 years)]
        (set! (.-innerHTML result-element)
          (str "You are about " days " days old."))))
    
    (set! (.-onclick button-element) calculate)
    
There’s a lot here, so let’s get started. First, ignore everything to the right of the ClojureScript code. That’s what the ClojureScript looks like after it has been translated to JavaScript. If you know JavaScript it may be interesting to you. For now, concentrate on the ClojureScript at the left.

The first three ``def``\ s bind the input text field, the button, and the result paragraph to symbols; these are for ease of reading in the rest of the code.

The ``calculate`` function is an *event handler*. Event handlers have one parameter: the JavaScript event object that caused the function to be called. In this instance, the code doesn’t need any of the event information. (Sometimes this information is useful; for example, a mouse click event carries properties telling where you clicked on the screen, which mouse button was pressed, etc.)

The first ``let`` binding gets the ``value`` property of the input element. This value is always a string, so the code must ``js/parseInt`` to convert it to a number.
The next binding calculates the result that goes on the screen.

Finally, the ``set!`` function sets the ``innnerHTML`` property of the result paragraph to a string that informs the user how old they are in days. (``innerHTML`` means “the HTML that is between the opening and closing tag of the element.”)

Now you have the code that handles the mouse click event, you need to associate it with the button. That is what the last expression in the code does, by setting the button’s ``onclick`` property to refer to the ``calculate`` function.

.. note::
    
    There is also an ``addEventListener`` function that you can use to associate the mouse click event with the calculate function. Depending upon whom you talk to,
    it is superior to ``onclick``. Your mileage may vary.



