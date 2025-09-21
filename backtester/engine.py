import pandas as pd

def backtest_single(price: pd.Series, signal: pd.Series, cost_bps: float = 5.0) -> pd.DataFrame:
    """
    very simple vector backtest for one asset:
    - position is yesterday's signal (avoid look-ahead)
    - costs are paid on position changes (turnover)
    - returns are simple daily pct changes
    """
    df = pd.DataFrame(index=price.index)
    df["price"] = price.astype(float)
    df["ret"] = df["price"].pct_change().fillna(0.0)

    # hold yesterday's signal
    pos = signal.reindex(df.index).fillna(0.0).clip(-1, 1)
    df["pos"] = pos.shift(1).fillna(0.0)

    # turnover = abs change in position
    df["turnover"] = df["pos"].diff().abs().fillna(df["pos"].abs())
    per_turnover_cost = cost_bps / 1e4  # bps -> decimal

    df["gross"] = df["pos"] * df["ret"]
    df["cost"]  = -per_turnover_cost * df["turnover"]
    df["net"]   = df["gross"] + df["cost"]
    df["equity"] = (1.0 + df["net"]).cumprod()

    return df
