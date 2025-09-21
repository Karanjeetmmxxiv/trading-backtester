import pandas as pd
import numpy as np

def sma_crossover(price: pd.Series, fast: int = 20, slow: int = 50) -> pd.Series:
    fast_ma = price.rolling(fast).mean()
    slow_ma = price.rolling(slow).mean()
    sig = (fast_ma > slow_ma).astype(int).diff().fillna(0)
    return sig

def momentum(price: pd.Series, lookback: int = 120) -> pd.Series:
    # sign of L-day return: +1 if up vs L days ago, -1 if down, 0 if flat
    mom = price.pct_change(lookback)
    sig = (mom > 0).astype(int) - (mom < 0).astype(int)
    # convert regime to entry/exit impulses (optional): keep as regime for engine
    return sig.rename("signal")

def mean_reversion(price: pd.Series, lookback: int = 20, z_entry: float = 1.0) -> pd.Series:
    r = price.pct_change()
    mu = r.rolling(lookback).mean()
    sd = r.rolling(lookback).std(ddof=0)
    z = (r - mu) / sd
    sig = pd.Series(0, index=price.index, dtype=float)
    sig[z < -z_entry] = 1.0   # oversold → long
    sig[z >  z_entry] = -1.0  # overbought → short
    return sig.rename("signal")
