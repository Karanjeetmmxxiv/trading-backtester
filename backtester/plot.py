import matplotlib.pyplot as plt

def plot_equity(df, equity_col="equity", title="Equity"):
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(df.index, df[equity_col])
    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Equity (x)")
    fig.tight_layout()
    return fig
