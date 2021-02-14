import json
import urllib.request
from binance.client import Client
import config
import sys

# TODO: change to API request : https://api.binance.com/api/v3/ticker/price

BASE_URL = 'https://api.binance.com'

# Get the keys from files
try:
    with open('API_SECRET.txt') as secret:
        API_SECRET = str(secret.read())
except FileNotFoundError:
    print("Error: Secret file not found, must be named API_SECRET.txt")
    sys.exit(1)
try:
    with open('API_KEY.txt') as key:
        API_KEY = str(key.read())
except FileNotFoundError:
    print("Error: Key file not found, must be named API_KEY.txt")
    sys.exit(2)

print(f"API KEY: {API_KEY}")
print(f"API SECRET: {API_SECRET}")

client = Client(API_KEY, API_SECRET)

print(client.get_asset_balance(asset='EUR'))

URL = "https://api.binance.com/api/v3/ticker/price"

response = urllib.request.urlopen(URL)
json_data = json.loads(response.read())

trading_pairs = []
# Get markets/trading pairs
for index in range(0, len(json_data)):
    if json_data[index]['symbol'][-3:] == "BTC":
        trading_pairs.append(json_data[index]['symbol'])
json_data[index]['symbol']

print("AVAILABLE MARKETS: ")
for market in trading_pairs:
    print(market)

while(True):
    chosen_market = ""
    input_trading = input("Input market name: ")

    for symbol in trading_pairs:
        chosen_market = ""
        if symbol[:-3] == input_trading.upper():
            print(symbol + " market found in currently trading BTC markets list")
            chosen_market = symbol
            break
    if chosen_market == "":
        print("Market not found")

        # FOUND MARKET. Start trading logic
