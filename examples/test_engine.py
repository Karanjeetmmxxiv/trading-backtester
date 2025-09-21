from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover
from backtester.engine import backtest_single
from backtester.metrics import sharpe, max_drawdown

# 1) data
px = priceloader_yf("AAPL", start="2018-01-01")

# 2) signal
sig = sma_crossover(px, fast=20, slow=50)

# 3) backtest
res = backtest_single(px, sig, cost_bps=5.0)
print(res.head())
print("final equity:", float(res["equity"].iloc[-1]))

# 4) metrics
sr = sharpe(res["net"])
mdd, mdd_s, mdd_e = max_drawdown(res["equity"])
print("sharpe:", sr)
print("max dd:", mdd, "from", mdd_s, "to", mdd_e)
