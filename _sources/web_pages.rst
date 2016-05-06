..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Accessing Web Pages
::::::::::::::::::::

Up to this point, your interaction with JavaScript has only been making calls to its functions. You may also have noticed that all the input for the functions have come from arguments that you have entered in ClojureScript. Modifying a previous example:
    
.. activecode:: symbol_def
    :caption: Input in Code
    :language: clojurescript
    
    (defn age-in-days [years]
      (* years 365))
    
    (age-in-days 62)
    
That works for me at my present age, but you probably aren’t 62 years old, and even if you are, next year both you and I will be older, so we will have to change the argument to ``age-in-days``. That’s OK for us; we’re programmers and we are cool with that :) We can’t, however, expect people using our programs to go rooting around in our code to get the results they want.
    
But for people who are used to web pages, you want to write HTML like this:
    
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

   <div style="border: 1px solid gray; padding: 0.25em">
   <p>
   Enter your age in years:
       <input type="text" id="years" />
       <input type="button" id="calculate"
         value="Calculate age in days"/>
   </p>
   <p id="result"></p>
   </div>
    
   
...where they can enter their age in years, click a button, and see a result. Here is code that does exactly that:
 
.. activecode:: interact
    :language: clojurescript
    :caption: Simple interaction
    
    (def input-element (.getElementById js/document "years"))
    (def button-element (.getElementById js/document "calculate"))
    (def result-element (.getElementById js/document "result"))
    
    (defn calculate [evt]
      (let [years (js/parseInt (.-value input-element))
            days (* 365 years)]
        (set! (.-innerHTML result-element)
          (str "You are about " days " days old."))))
    
    ; (set! (.-onclick button-element) calculate)
    
  


