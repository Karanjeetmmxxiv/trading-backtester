from backtester.data import priceloader_yf

aapl = priceloader_yf("AAPL", start="2018-01-01")
print("AAPL head:\n", aapl.head())
print("AAPL len:", len(aapl))

btc = priceloader_yf("BTC-USD", start="2018-01-01", use_adjusted=False)
print("\nBTC-USD tail:\n", btc.tail())
print("BTC NaNs:", btc.isna().sum())
