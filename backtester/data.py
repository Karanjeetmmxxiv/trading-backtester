import pandas as pd
import yfinance as yf

def priceloader_yf(ticker: str, start="2015-01-01", end=None, use_adjusted=True):
    df = yf.download(ticker, start=start, end=end, auto_adjust=False, progress=False)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ["_".join([str(c) for c in col if c]) for col in df.columns]

    if df.empty:
        raise ValueError(f"no data for {ticker}")

    cols = [str(c) for c in df.columns]

    def match_col(name: str):
        # loosen the matching so it works with suffixes like "_AAPL"
        name = name.lower().replace(" ", "")
        for c in cols:
            check = c.lower().replace(" ", "").replace("_", "")
            if check.endswith(name) or name in check:
                return c
        return None

    col = match_col("AdjClose") if use_adjusted else None
    if not col:
        col = match_col("Close")
    if not col:
        raise ValueError(f"can't find a price column in {cols}")

    price = df[col].astype(float)
    price.name = "price"
    price.index = pd.to_datetime(price.index, utc=True)
    price = price.sort_index()

    if price.isna().any():
        raise ValueError("price series has NaNs")
    if not price.index.is_monotonic_increasing:
        raise ValueError("dates not sorted properly")

    return price
