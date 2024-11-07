import yfinance as yf
import matplotlib.pyplot as plt

stock_data = yf.download('AAPL', start='2023-01-01', end='2024-01-01')

print(stock_data.head())

stock_data['Close'].plot(title='AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
