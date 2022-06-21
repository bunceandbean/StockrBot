import yfinance as yf
from visualization.ticker import render_ticker

msft = yf.Ticker("MSFT")
render_ticker(msft)
