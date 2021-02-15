def get_pairs(json_data):
    trading_pairs = []
    # Get markets/trading pairs
    for index in range(0, len(json_data)):
        if json_data[index]['symbol'][-3:] == "BTC":
            trading_pairs.append(json_data[index]['symbol'])
    return trading_pairs


def print_markets(trading_pairs):
    print("AVAILABLE MARKETS: ")
    for market in trading_pairs:
        print(market[:-3])


def get_market(trading_pairs):
    while(True):
        chosen_market = ""
        input_trading = input("Input symbol: ")

        for symbol in trading_pairs:
            chosen_market = ""
            if symbol[:-3] == input_trading.upper():
                print(symbol + " market found in currently trading BTC markets list")
                chosen_market = symbol
                return chosen_market
        if chosen_market == "":
            print("Market not found")
