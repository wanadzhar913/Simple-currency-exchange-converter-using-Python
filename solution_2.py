# We'll be using the 'requests' library from python.
import requests
from datetime import datetime

# We now define variables of interest. 

rate_date = str(input("Enter the date you'd like the exchange rate to be on (yyyy-mm-dd): "))
str_to_date = datetime.strptime(rate_date, '%Y-%m-%d').date()

from_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()

to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(f'''https://api.frankfurter.app/latest?amount={amount}&date={str_to_date}&from={from_currency}&to={to_currency}''')

# print(response.status_code) 
# The above line of code returns a number that indicates the status (200 is OK, 404 is Not Found). 
# You can read more at this link: https://www.geeksforgeeks.org/response-status_code-python-requests/

# output (amount in converted currency)
print(f'''{amount} {from_currency} is {response.json()['rates'][to_currency]}{to_currency} on {rate_date}''')

