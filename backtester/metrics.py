import numpy as np
import pandas as pd

def sharpe(net: pd.Series, periods: int = 252) -> float:
    mu = net.mean()
    sd = net.std(ddof=0)
    if sd == 0 or np.isnan(sd):
        return np.nan
    return (mu * np.sqrt(periods)) / sd

def max_drawdown(equity: pd.Series):
    peak = equity.cummax()
    dd = equity / peak - 1.0
    mdd = dd.min()
    end = dd.idxmin()
    start = equity.loc[:end].idxmax()
    return float(mdd), start, end
