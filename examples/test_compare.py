from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover, momentum, mean_reversion
from backtester.engine import backtest_single
from backtester.metrics import sharpe, max_drawdown

px = priceloader_yf("AAPL", start="2018-01-01")

tests = {
    "SMA(20,50)": sma_crossover(px, 20, 50),
    "Momentum(120)": momentum(px, 120),
    "MeanRev(20,z=1.0)": mean_reversion(px, 20, 1.0),
}

for name, sig in tests.items():
    res = backtest_single(px, sig, cost_bps=5.0)
    sr = sharpe(res["net"])
    mdd, s, e = max_drawdown(res["equity"])
    final = float(res["equity"].iloc[-1])
    print(f"\n{name}")
    print(f"  Final Equity: {final:.3f}")
    print(f"  Sharpe:      {sr:.2f}")
    print(f"  Max DD:      {mdd:.2%}  ({s} → {e})")
