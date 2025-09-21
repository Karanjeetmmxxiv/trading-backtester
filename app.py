import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from backtester.data import priceloader_yf
from backtester.strategies import sma_crossover, momentum, mean_reversion
from backtester.engine import backtest_single
from backtester.metrics import sharpe, max_drawdown
from backtester.plot import plot_equity

st.set_page_config(page_title="Trading Strategy Backtester", layout="centered")
st.title("Trading Strategy Backtester")

ticker = st.text_input("Ticker (e.g. AAPL, BTC-USD)", "AAPL").strip()
start_date = st.date_input("Start Date", value=pd.to_datetime("2018-01-01")).strftime("%Y-%m-%d")
strategy = st.selectbox("Strategy", ["SMA Crossover", "Momentum", "Mean Reversion"])

if strategy == "SMA Crossover":
    fast = st.slider("Fast SMA", 5, 50, 20)
    slow = st.slider("Slow SMA", 20, 200, 50)
elif strategy == "Momentum":
    lb = st.slider("Lookback (days)", 20, 252, 120)
else:
    lb = st.slider("Lookback (days)", 5, 50, 20)
    z = st.slider("Z-Score Entry", 0.5, 3.0, 1.0)

cost_bps = st.slider("Trading cost (bps per turnover)", 0, 50, 5)

def is_crypto(sym: str) -> bool:
    s = sym.upper()
    return s.endswith("-USD") or s.endswith("-USDT")

@st.cache_data(show_spinner=False)
def fetch_price(ticker: str, start: str, use_adjusted: bool):
    return priceloader_yf(ticker, start=start, use_adjusted=use_adjusted)

if st.button("Run Backtest", type="primary"):
    try:
        use_adj = not is_crypto(ticker)
        with st.spinner("Fetching data and running backtest..."):
            px = fetch_price(ticker, start_date, use_adj)

            if strategy == "SMA Crossover":
                sig = sma_crossover(px, fast=fast, slow=slow)
                title = f"SMA({fast},{slow}) on {ticker}"
            elif strategy == "Momentum":
                sig = momentum(px, lookback=lb)
                title = f"Momentum({lb}) on {ticker}"
            else:
                sig = mean_reversion(px, lookback=lb, z_entry=z)
                title = f"MeanReversion({lb}, z={z}) on {ticker}"

            res = backtest_single(px, sig, cost_bps=cost_bps)
            sr = sharpe(res["net"])
            mdd, s, e = max_drawdown(res["equity"])
            final_eq = float(res["equity"].iloc[-1])

        st.subheader("Results")
        col1, col2, col3 = st.columns(3)
        col1.metric("Final Equity (×)", f"{final_eq:.3f}")
        col2.metric("Sharpe", f"{sr:.2f}")
        col3.metric("Max Drawdown", f"{mdd:.2%}")

        fig = plot_equity(res, title=title)
        st.pyplot(fig)

    except Exception as err:
        st.error(f"Error: {err}")
