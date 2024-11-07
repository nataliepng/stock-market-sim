import yfinance as yf
class Portfolio:
    def __init__(self, initial_balance=10000):
        self.balance = initial_balance
        self.holdings = {}  # Format: {ticker: {'quantity': int, 'avg_price': float}}

    def get_current_price(self, ticker):
        stock = yf.Ticker(ticker)
        history = stock.history(period="1d")
    
        if history.empty:
            print(f"Error: {ticker} is invalid or may be delisted. No price data found.")
            return None
    
    # Safely access the first available price
        try:
            price = history['Close'].iloc[0]  # Use .iloc to safely access by position
            return price
        except IndexError:
            print("Failed to retrieve price data.")
            return None


    def sell_stock(self, ticker, quantity, price):
        if ticker in self.holdings and self.holdings[ticker]['quantity'] >= quantity:
            self.balance += quantity * price
            self.holdings[ticker]['quantity'] -= quantity
            if self.holdings[ticker]['quantity'] == 0:
                del self.holdings[ticker]
            print(f"Sold {quantity} shares of {ticker} at ${price}")
        else:
            print("Insufficient shares to sell")

    def view_portfolio(self):
        print("\nPortfolio:")
        for ticker, info in self.holdings.items():
            print(f"{ticker}: {info['quantity']} shares at avg price ${info['avg_price']:.2f}")
        print(f"Available balance: ${self.balance:.2f}")

    def buy_stock(self, ticker, quantity):
        price = self.get_current_price(ticker)
        if price is None:
            print(f"Could not buy {ticker}. Price data unavailable.")
            return
    
        total_cost = quantity * price
        if self.balance >= total_cost:
            self.balance -= total_cost
            if ticker in self.holdings:
                current_qty = self.holdings[ticker]['quantity']
                current_avg = self.holdings[ticker]['avg_price']
                new_qty = current_qty + quantity
                self.holdings[ticker] = {
                    'quantity': new_qty,
                    'avg_price': (current_avg * current_qty + total_cost) / new_qty
                }
            else:
                self.holdings[ticker] = {'quantity': quantity, 'avg_price': price}
            print(f"Bought {quantity} shares of {ticker} at ${price:.2f}")
        else:
            print("Insufficient balance")

    
my_portfolio = Portfolio(initial_balance=10000)

# User interaction loop
while True:
    action = input("\nChoose an action: [buy/sell/view/exit]: ").strip().lower()
    if action == "buy":
        ticker = input("Enter stock ticker: ").upper()
        quantity = int(input("Enter quantity to buy: "))
        my_portfolio.buy_stock(ticker, quantity)
    elif action == "sell":
        ticker = input("Enter stock ticker: ").upper()
        quantity = int(input("Enter quantity to sell: "))
        my_portfolio.sell_stock(ticker, quantity)
    elif action == "view":
        my_portfolio.view_portfolio()
    elif action == "exit":
        print("Exiting portfolio manager.")
        break
    else:
        print("Invalid action. Please try again.")
