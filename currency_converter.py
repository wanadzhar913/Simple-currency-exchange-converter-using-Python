# We'll be using the 'requests' library and 'datetime' module from python.
import requests

# We restrict the type of currencies we can convert from and to. 
iso_codes = requests.get('https://api.frankfurter.app/currencies')
iso_codes_only = list(iso_codes.json().keys())

# We now define the variables of interest.
# Currency to convert from. 
from_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()
while from_currency not in iso_codes_only:
    print('Plese enter a valid country code.')
    from_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()

# Currency to convert to.
to_currency = str(input("Enter in the currency you'd like to convert to: ")).upper()
while to_currency not in iso_codes_only:
    print('Plese enter a valid country code.')
    to_currency = str(input("Enter in the currency you'd like to convert from: ")).upper()

# Amount of currency to convert.
while True:
    try:
        amount = float(input("Enter in the amount of money you'd like to convert: "))
        while amount < 0:
            print('Please enter a positive amount.')
            amount = float(input("Enter in the amount of money you'd like to convert: "))
    except ValueError as e:
        print("Error: {}".format(e), end = '\n')
        print("Please enter a valid amount.")
    except:
        print("Please enter a suitable date in the required format.")
    else:
        break

response = requests.get(f'''https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}''')

# The line of code below returns a number that indicates the status (200 is OK, 404 is Not Found). 
# You can read more at this link: https://www.geeksforgeeks.org/response-status_code-python-requests/
print('Status code: {}'.format(response.status_code)) 

# output (amount in converted currency)
print(f'''Per today's exchange rate, {amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}.''')