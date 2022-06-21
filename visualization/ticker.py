import pyfiglet as fig
from visualization.tools import bcolors

def render_ticker(ticker):
 print(bcolors["OKCYAN"] +fig.figlet_format(ticker, font = "slant") + bcolors["ENDC"])
