from urllib import response
import requests
import os
import time

# To work with the .env file
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"
symbols = [
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
    "AAPL",
    "GOOG",
    "TSLA",
    "MSFT",
    "PEP",
]
results = []

for symbol in symbols:
    print(f"Fetching data for {symbol}")
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())

print(results)
