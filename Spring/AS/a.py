import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import binom


def binomial_option_pricing(S, K, T, r, sigma, n, option_type="call", american=False):
    dt = T / n  # Time step
    u = np.exp(sigma * np.sqrt(dt))  # Up factor
    d = 1 / u  # Down factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    # Stock price tree
    stock_tree = np.zeros((n + 1, n + 1))
    for i in range(n + 1):
        for j in range(i + 1):
            stock_tree[j, i] = S * (u ** (i - j)) * (d ** j)

    # Option value at maturity
    option_tree = np.zeros((n + 1, n + 1))
    if option_type == "call":
        option_tree[:, -1] = np.maximum(stock_tree[:, -1] - K, 0)
    else:
        option_tree[:, -1] = np.maximum(K - stock_tree[:, -1], 0)

    # Backward induction
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            option_tree[j, i] = np.exp(-r * dt) * (p * option_tree[j, i + 1] + (1 - p) * option_tree[j + 1, i + 1])
            if american:
                if option_type == "call":
                    option_tree[j, i] = max(option_tree[j, i], stock_tree[j, i] - K)
                else:
                    option_tree[j, i] = max(option_tree[j, i], K - stock_tree[j, i])

    return option_tree[0, 0], stock_tree, option_tree


# Fetch current stock price of AAPL
aapl = yf.Ticker("AAPL")
S = aapl.history(period="1d")['Close'].iloc[-1]

# Define parameters
K = S * 1.05  # Strike price (5% above current price)
T = 1  # Time to maturity (1 year)
r = 0.05  # Risk-free rate (5%)
sigma = 0.2  # Volatility (20%)
n = 10  # Number of time steps (lowered for visualization)

# Calculate option prices
call_price, stock_tree, option_tree = binomial_option_pricing(S, K, T, r, sigma, n, "call", american=False)
put_price, _, _ = binomial_option_pricing(S, K, T, r, sigma, n, "put", american=False)

print(f"European Call Option Price: {call_price:.2f}")
print(f"European Put Option Price: {put_price:.2f}")

# Plot stock price tree
plt.figure(figsize=(10, 6))
for i in range(n + 1):
    plt.plot([i] * (i + 1), stock_tree[:i + 1, i], 'bo', alpha=0.6)
plt.xlabel("Time Steps")
plt.ylabel("Stock Price")
plt.title("Binomial Tree for AAPL Stock Price")
plt.grid()
plt.show()