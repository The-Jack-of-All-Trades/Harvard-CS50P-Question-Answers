import requests
import sys

try:
    if len(sys.argv) != 2:
        raise requests.RequestException

    try:

        bitcoin_amount = float(sys.argv[1])

        api_key = "REPLACE THIS TEXT WITH YOUR API KEY!!!"

        response = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}")

        output = response.json()

        price = float(output["data"]["priceUsd"])

        total = price * bitcoin_amount

        print(f"${total:,.4f}")

    except ValueError:
        raise requests.RequestException

except requests.RequestException:
    print("Missing command-line argument")
    sys.exit()
