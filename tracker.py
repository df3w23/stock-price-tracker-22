import sys
import random

class StockTracker:
    def __init__(self):
        # Mock data for demonstration purposes
        self.stocks = {
            "AAPL": 175.50,
            "MSFT": 420.12,
            "GOOGL": 142.30,
            "AMZN": 178.22,
            "TSLA": 163.57
        }

    def get_price(self, ticker):
        ticker = ticker.upper()
        if ticker in self.stocks:
            # Add a small random fluctuation to simulate live movement
            fluctuation = random.uniform(-1.0, 1.0)
            return round(self.stocks[ticker] + fluctuation, 2)
        return None

    def run(self):
        print("--- Stock Price Tracker 2022 v1.0 ---")
        print("Enter 'quit' to exit.")
        while True:
            symbol = input("Enter Stock Ticker (e.g., AAPL): ").strip().upper()
            if symbol == 'QUIT':
                break
            
            price = self.get_price(symbol)
            if price:
                print(f"The current price of {symbol} is: ${price}")
            else:
                print(f"Ticker '{symbol}' not found in watch list.")

if __name__ == '__main__':
    tracker = StockTracker()
    try:
        tracker.run()
    except KeyboardInterrupt:
        sys.exit(0)