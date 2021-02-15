import parse_symbols
import sys
import urllib
import json
from binance.client import Client

BASE_URL = 'https://api.binance.com'


def getkeys():
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

    return API_KEY, API_SECRET


if __name__ == '__main__':
    API_KEY, API_SECRET = getkeys()

    client = Client(API_KEY, API_SECRET)

    print(client.get_asset_balance(asset='EUR'))

    URL = "https://api.binance.com/api/v3/ticker/price"

    response = urllib.request.urlopen(URL)
    json_data = json.loads(response.read())
    trading_pairs = parse_symbols.get_pairs(json_data)

    parse_symbols.print_markets(trading_pairs)
    parse_symbols.get_market(trading_pairs)
    print("Executing trade logic...")
    sys.exit(0)
