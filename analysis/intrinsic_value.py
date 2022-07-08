from data.read_write import load_from_json

def intrinsic_value(ticker):
    stockinfo = load_from_json(ticker)
    