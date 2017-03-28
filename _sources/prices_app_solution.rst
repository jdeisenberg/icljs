..  Copyright © J David Eisenberg
.. |---| unicode:: U+2014  .. em dash, trimming surrounding whitespace
   :trim:

Price and Discount Solution
''''''''''''''''''''''''''''

Here is my proposed solution for the price and discount problem described on the previous page.
Your solution will almost certainly not look like mine, since everyone has their own way of
solving problems and writing programs. I have deliberately used many small functions for
clarity rather than having a few large functions, so your solution may be more compact.
    
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

Ignore the code in the right-hand panel. You should be able to fill in the form fields and then
click the button to see the program in action.

.. activecode:: price_program
    :language: clojurescript
    :autorun:
    :caption: Price Program
    
    (defn get-input-field
      "Convenience function to retrieve value of an input field"
      [id]
      (.-value (.getElementById js/document id)))

    (defn get-element
      "Convenience function to retreive an element by its id"
      [id]
        (.getElementById js/document id))
    
    (defn get-discount-as-decimal
      "Convert input field to decimal"
      []
      (let [s (get-input-field "discount")]
        (/ (js/parseFloat s) 100)))
        
    (defn monetize
      "Convert item to currency format with two decimal places"
      [item]
      (str "$" (.toFixed item 2)))
    
    (defn list-item
      "Create an HTML list item"
      [item]
      (str "<li>" item "</li>"))

    (defn to-unordered-list
      "Convert a list of numbers to a string that
      represents an HTML unordered list"
      [prices]
      (let [money (map monetize prices)
            li-list (map list-item money)
            list-item-string (reduce str li-list)]
        (str "<ul>" list-item-string "</ul>")))

    (defn true-number
      "Function for filter; keeps things that are numbers and
      eliminates NaNs."
      [x]
      (not (js/isNaN x)))
    
    (defn to-valid-numbers
      "Given a list of string, return a list of floats
      with non-numerics eliminated"
      [string-list]
      (->> string-list
        (map js/parseFloat)
        (filter true-number)))
    
    (defn calc-one-price
      "Apply a discount to a price"
      [discount price]
      (* (- 1 discount) price))
    
    (defn calc-discount-prices
      "Get discount from web form and apply it to the
      list of prices"
      [prices]
      (let [discount (get-discount-as-decimal)
            discount-fcn (partial calc-one-price discount)]
        (map discount-fcn prices)))
        
    (defn calculate [evt]
      (let [price-str (get-input-field "prices")
            price-list (.split price-str " ")
            price-numbers (to-valid-numbers price-list)
            discount-prices (calc-discount-prices price-numbers)
            output-str (to-unordered-list discount-prices)]
        (set! (.-innerHTML (get-element "result"))
        output-str)))
        
    (set! (.-onclick (get-element "calculate")) calculate)    
