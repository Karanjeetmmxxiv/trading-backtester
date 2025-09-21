# Trading Backtester

A simple Python backtester I built to practice working with market data and trading ideas.
It pulls prices from Yahoo Finance and lets me try out classic strategies like moving average crossover, momentum, and mean reversion.

## What it does

Fetches stock/crypto data with yfinance

Runs basic strategies (SMA crossover, momentum, mean reversion)

Backtests with trading costs and position sizing

Reports Sharpe ratio, max drawdown, and final equity

Includes small example scripts to test each piece

##Interactive App (Streamlit)

You can run the Streamlit frontend to explore strategies without touching code:

streamlit run app.py

Here is the app

https://trading-backtester-4bpbzerv5r3sbn6b7ofktx.streamlit.app/

This opens a browser app where you can:

Enter a ticker (e.g. AAPL, BTC-USD)

Choose a start date

Select a strategy (SMA crossover, momentum, mean reversion)

Adjust parameters with sliders

View metrics (Sharpe, Max Drawdown, Final Equity) and equity curve plots

## Demo Notebook

For a code-first walkthrough, see demo.ipynb
.
It shows how to:

Fetch data with yfinance

Run SMA/Momentum/Mean Reversion

Backtest with transaction costs

## Plot equity curves

Quickstart

git clone https://github.com/Karanjeetmmxxiv/trading-backtester.git
cd trading-backtester
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
python -m examples.run_demo

Example Equity Curve

<img width="789" height="393" alt="image" src="https://github.com/user-attachments/assets/2eaa6e1a-29e6-486f-ae67-cc53b2fb0b7b" />

