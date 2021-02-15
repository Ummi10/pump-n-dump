import json
import urllib.request
from binance.client import Client
import config
import sys
import os

# TODO: change to API request : https://api.binance.com/api/v3/ticker/price

BASE_URL = 'https://api.binance.com'

API_KEY = os.environ.get('binance_api')
API_SECRET = os.environ.get('binance_secret')

client = Client(config.API_KEY, config.API_SECRET, tld='com')
# Get BTC account balance
accountBalance = client.get_asset_balance(asset='BTC')
accountBalance = accountBalance['free']
print("Current BTC account balance is " + accountBalance)

# Get all available markets
URL = "https://api.binance.com/api/v3/ticker/price"
response = urllib.request.urlopen(URL)
json_data = json.loads(response.read())

trading_pairs = []
# Get markets/trading pairs
for index in range(0, len(json_data)):
    if json_data[index]['symbol'][-3:] == "BTC":
        trading_pairs.append(json_data[index]['symbol'])
json_data[index]['symbol']


while(True):
    #Get trading ammount
    tradingAmmount = 0
    while True:
        tradingAmmount = input("How much BTC do you want to use for buying (0-"+accountBalance+"): ")
        if tradingAmmount < = accountBalance and tradingAmmount > 0:
            getConfirmation = input("Are you sure you want to buy for  + tradingAmmount ? (y/n) ")
            if getConfirmation.lower() == 'y':
                break
            else:
                print("Invalid trading ammount entered")
    
    # Choose market to trade in
    chosen_market = ""
    input_trading = input("Input market name: ")
    #TODO: FIX ERROR - WHEN INVALID MARKET IS TAKEN AS INPUT YOU HAVE TO INSERT TRADING AMMOUTN AGAIN
    for symbol in trading_pairs:
        chosen_market = ""
        if symbol[:-3] == input_trading.upper():
            print(symbol + " market found in currently trading BTC markets list")
            chosen_market = symbol
            break
    if chosen_market == "":
        print("Market not found")
  
        # Start buying
        # 1. Get the chosen market price and convert using conversion rate and tradingAmmount BTC value to symbol quantity
        # .
        
