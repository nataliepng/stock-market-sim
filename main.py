import yfinance as yf
import matplotlib.pyplot as plt

# Fetch stock data for AAPL (Apple Inc.)
stock_data = yf.download('AAPL', start='2023-01-01', end='2024-01-01')

# Display the first few rows of the stock data
print(stock_data.head())

# Plot the closing prices
stock_data['Close'].plot(title='AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
