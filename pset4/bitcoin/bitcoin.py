import sys
import requests

#for CLI
if len(sys.argv) !=2:
    print("Missing Command Line argument")
    sys.exit(1)

#for str --> float
try:
    btc = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

#for BTC-->USD
try:
    response = requests.get("https://rest.coincap.io/v3/assets?apiKey=427519f882c415aef0283e30411bb4bbead7f00615f5299a62e5b5f30def3d73")
    content = response.json()
    price = content["data"]["priceUsd"]
    amount = float(price)

except requests.RequestException:
    print("Error")
    sys.exit(1)

tp = amount*btc
print(f"${tp:,.4f}")



