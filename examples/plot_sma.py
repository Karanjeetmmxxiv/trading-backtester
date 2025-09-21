from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover
from backtester.engine import backtest_single
from backtester.plot import plot_equity
import matplotlib.pyplot as plt

px = priceloader_yf("AAPL", start="2018-01-01")
sig = sma_crossover(px, 20, 50)
res = backtest_single(px, sig, cost_bps=5.0)
plot_equity(res, title="SMA(20,50) on AAPL")
plt.show()
