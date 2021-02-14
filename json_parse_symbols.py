import json
import urllib.request
# TODO: change to API request : https://api.binance.com/api/v3/ticker/price

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
