import matplotlib.pyplot as plt
from datetime import datetime
from polygon import RESTClient

client = RESTClient(api_key="api_key")
ticker = "AAPL"

# List Aggregates (Bars)
timestamps = []
closing_prices = []

for agg in client.list_aggs(ticker=ticker, multiplier=1, timespan="month", from_="2023-01-01", to="2024-01-30", limit=50000):
    print(agg)
    timestamps.append(datetime.fromtimestamp(agg.timestamp / 1000))  # Convert timestamp to datetime object
    closing_prices.append(agg.close)  # Closing price

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(timestamps, closing_prices, marker='o', linestyle='-', color='b')
plt.title(f"Closing Prices for {ticker} (2023-01-01 to 2023-01-05)")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()
