import yfinance as yf
from visualization.ticker import render_ticker
from visualization.tools import bcolors

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

main()
