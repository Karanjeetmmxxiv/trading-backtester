from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover

# fetch AAPL price data
aapl = priceloader_yf("AAPL", start="2018-01-01")

# generate SMA crossover signals
signals = sma_crossover(aapl, fast=20, slow=50)

print("Signals head:\n", signals.head(60))   # first 60 days
print("Unique signal values:", signals.unique())
