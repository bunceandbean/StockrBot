import sys
import pyfiglet as fig
from visualization.tools import bcolors

def render_ticker(ticker):
    try:
        print(bcolors["OKBLUE"] + fig.figlet_format(ticker.info["symbol"], font = "slant") + bcolors["ENDC"])
        try:
            print(bcolors["OKGREEN"] + "Current Price: " + str(ticker.info["currentPrice"]) + bcolors["ENDC"])
        except:
            print(bcolors["WARNING"] + "Warning: Unknown or volatile data." + bcolors["ENDC"])
    except:
        print(bcolors["FAIL"] + "Error: Argument for render_ticker() was not a Ticker object." + bcolors["ENDC"])
        sys.exit()
