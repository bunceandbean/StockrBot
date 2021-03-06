import yfinance as yf
from visualization.ticker import render_ticker
from visualization.tools import bcolors
from data.read_write import save_to_json

def main():
    tick_input = ''
    ticker_dict = {"ticker":[]}

    while True:
        tick_input = str(input(bcolors["OKGREEN"] + "Enter ticker symbol or write 'exit' to leave: " + bcolors["ENDC"])).lower()
        if tick_input == 'exit':
            break
        tick = yf.Ticker(tick_input)

        #If the ticker does not exist, it will return an object with 9 default elements.
        #This checks for more than 9 elements to see if it is a valid ticker.

        while len(tick.info) < 10:
            tick_input = str(input(bcolors["WARNING"] + "Error: Invalid ticker symbol. Try again, or write 'exit' to leave: " + bcolors["ENDC"])).lower()
            if tick_input == 'exit':
                break
            tick = yf.Ticker(tick_input)
        render_ticker(tick)
        rw_input = str(input("Write the ticker data to Saves/" + tick.info["symbol"] + ".json? y/n: ")).lower()
        if rw_input.lower() == 'y':
            save_to_json(tick.info, tick.info["symbol"], "Saves/")
            ticker_dict["ticker"].append(tick.info["symbol"])
    
    save_to_json(ticker_dict,"save_info", "data/")

main()
