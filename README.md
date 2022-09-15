### Simple-currency-exchange-converter-using-Python

I came across a simple online tutorial for how to create a currency exchange converter using Python. The tutorial can be found [here](https://www.youtube.com/watch?v=snPGUT-Fxa4).

It makes use of the [Frankfurter API](https://github.com/hakanensari/frankfurter). In their own words, Frankfurter API are an *open-source API for current and historical foreign exchange rates published by the European Central Bank (ECB)*.

I have since modified the code with more robust exception handling, extracted an additional variable (date), limited the currencies that can be converted to and from (per ECB's availability), as well as set a date range for inputs. Overall, this project briefly introduced me to Python's Requests library and datetime module, as well as help practice my exception handling.