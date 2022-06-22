import yfinance as yf
from visualization.ticker import render_ticker
from visualization.tools import bcolors
from data.read_write import save_to_json

def main():
    tick_input = str(input(bcolors["OKGREEN"] + "Enter ticker symbol or write 'exit' to leave: " + bcolors["ENDC"])).lower()
    if tick_input == 'exit':
        return
    tick = yf.Ticker(tick_input)
    while len(tick.info) < 10:
        tick_input = str(input(bcolors["WARNING"] + "Error: Invalid ticker symbol. Try again, or write 'exit' to leave: " + bcolors["ENDC"])).lower()
        if tick_input == 'exit':
            return
        tick = yf.Ticker(tick_input)
    render_ticker(tick)
    rw_input = str(input("Write the ticker data to Saves/" + tick.info["symbol"] + ".json? y/n: ")).lower()
    if rw_input.lower() == 'y':
        save_to_json(tick.info, tick.info["symbol"])

main()
