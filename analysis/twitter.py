import requests

URL = "https://api.twitter.com/2/tweets/search/recent?query=AAPL"
twitter = requests.get(URL)

