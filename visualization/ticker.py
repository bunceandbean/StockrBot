import sys
import pyfiglet as fig
from visualization.tools import bcolors

#Renders ticker information to the screen. Argument is a Ticker object.

def render_ticker(ticker):
    try:
        print(bcolors["OKBLUE"] + fig.figlet_format(ticker.info["symbol"], font = "slant") + ticker.info["shortName"] + bcolors["ENDC"])
        try:
            print(bcolors["BOLD"] + bcolors["OKGREEN"] + "Current Price: " + str(ticker.info["currentPrice"]) + bcolors["ENDC"] + bcolors["ENDC"])
            print(bcolors["OKBLUE"] + "#################################" + bcolors["ENDC"])
            print(bcolors["OKGREEN"] + "Day High: " + str(ticker.info["dayHigh"]) + bcolors["ENDC"])
            print(bcolors["FAIL"] + "Day Low: " + str(ticker.info["dayLow"]) + bcolors["ENDC"])
        except:
            print(bcolors["WARNING"] + "Warning: Unknown or volatile data." + bcolors["ENDC"])
    except:
        print(bcolors["FAIL"] + "Error: Argument for render_ticker() was not a Ticker object." + bcolors["ENDC"])
        sys.exit()
