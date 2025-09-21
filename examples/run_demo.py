# examples/run_demo.py
from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover, momentum, mean_reversion
from backtester.engine import backtest_single
from backtester.metrics import sharpe, max_drawdown

def run_one(name, price, signal):
    res = backtest_single(price, signal, cost_bps=5.0)
    sr = sharpe(res["net"])
    mdd, s, e = max_drawdown(res["equity"])
    final_eq = float(res["equity"].iloc[-1])
    print(f"\n{name}")
    print(f"  Final Equity: {final_eq:.3f}")
    print(f"  Sharpe:       {sr:.2f}")
    print(f"  Max DD:       {mdd:.2%} ({s} → {e})")
    return res

def main():
    # choose your asset here (AAPL = Apple stock)
    px = priceloader_yf("AAPL", start="2018-01-01")

    # build signals
    sig_sma = sma_crossover(px, fast=20, slow=50)
    sig_mom = momentum(px, lookback=120)
    sig_mr  = mean_reversion(px, lookback=20, z_entry=1.0)

    # run
    run_one("SMA(20,50)", px, sig_sma)
    run_one("Momentum(120)", px, sig_mom)
    run_one("MeanReversion(20, z=1.0)", px, sig_mr)

if __name__ == "__main__":
    main()
