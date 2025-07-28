import yfinance as yf
import pandas as pd
from datetime import datetime

# Add more stock codes as needed
symbols = ["RELIANCE.NS", "TCS.NS", "INFY.NS"]

for symbol in symbols:
    data = yf.download(symbol, period="5d", interval="1d")
    data.to_csv(f"data/{symbol.split('.')[0]}.csv")
    print(f"Fetched data for {symbol} at {datetime.now()}")
