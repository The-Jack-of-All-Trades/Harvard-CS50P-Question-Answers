import requests
import sys

try:
    if len(sys.argv) != 2: # If the users command line arguments is not equal to 2, then skip down to line 27 
        raise requests.RequestException # Just a specific error from the "requests" module

    try:

        bitcoin_amount = float(sys.argv[1]) # Convert the second command line argument (the first command line argument is "bitcion.py") to a float

        api_key = "REPLACE THIS TEXT WITH YOUR API KEY!!!" # This is your API key, you will need to get your own

        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}") # Use the "requests" module to retrieve data from the URL with your API key inserted into the URL

        output = response.json() # Convert the reponse to JSON

        price = float(output["data"]["priceUsd"]) # Accesses the block "data" inside "output" then in "data," it accesses the value from "priceUSD" that is inside the "data" block 

        total = price * bitcoin_amount

        print(f"${total:,.4f}") # Rounds the total to 4 decimal places and adds commas to every thousands value --> (1,000,000.0000)

    except ValueError: # When a "ValueError" occurs, it will instantly skip to line 27 by raising that error
        raise requests.RequestException

except requests.RequestException:
    print("Missing command-line argument")
    sys.exit() # This will instantly terminate the program, ending it immediately
