import csv
import os

class StockTracker:
    def __init__(self):
        self.stock_prices = {
            "AAPL": 180,
            "TSLA": 250,
            "GOOG": 140,
            "AMZN": 130
    
        self.portfolio = {}
        self.filename = "portfolio.csv"
        self.load_portfolio()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def load_portfolio(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        stock = row["Stock"]
                        quantity = int(row["Quantity"])
                        self.portfolio[stock] = quantity
        except Exception as e:
            print(f"Error loading portfolio: {e}")

    def save_portfolio(self, silent=False):
        try:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Stock", "Quantity", "Price", "Value"])
                for stock, quantity in self.portfolio.items():
                    price = self.stock_prices.get(stock, 0)
                    value = price * quantity
                    writer.writerow([stock, quantity, price, value])
            if not silent:
                print(f"Portfolio auto-saved to {self.filename}")
        except Exception as e:
            print(f"Error saving portfolio: {e}")

    def show_available_stocks(self):
        print("\n--- Available Stocks ---")
        for stock, price in self.stock_prices.items():
            print(f"{stock:5} : ${price}")
        print("-" * 25)

    def add_stock(self):
        self.show_available_stocks()
        stock = input("\nEnter stock symbol: ").upper()
        if stock not in self.stock_prices:
            print("❌ Stock not available!")
            return

        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            if quantity <= 0:
                print("❌ Quantity must be positive!")
                return
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            return

        self.portfolio[stock] = self.portfolio.get(stock, 0) + quantity
        print(f"✅ Added {quantity} shares of {stock}.")
        self.save_portfolio(silent=True)

    def remove_stock(self):
        stock = input("Enter stock symbol to remove: ").upper()
        if stock in self.portfolio:
            del self.portfolio[stock]
            print(f"✅ {stock} removed from portfolio.")
            self.save_portfolio(silent=True)
        else:
            print("❌ Stock not found in portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("\n📭 Portfolio is empty.")
            return

        total_value = sum(qty * self.stock_prices[s] for s, qty in self.portfolio.items())
        
        print("\n" + "="*60)
        print(f"{'STOCK':<10} {'QTY':<8} {'PRICE':<10} {'VALUE':<12} {'WEIGHT':<8}")
        print("-" * 60)

        for stock, quantity in self.portfolio.items():
            price = self.stock_prices[stock]
            value = price * quantity
            weight = (value / total_value) * 100
            print(f"{stock:<10} {quantity:<8} ${price:<9} ${value:<11.2f} {weight:>6.1f}%")

        print("-" * 60)
        print(f"{'TOTAL PORTFOLIO VALUE:':<30} ${total_value:>11.2f}")
        
        # Diversification Analysis
        if len(self.portfolio) < 3:
            print("\n⚠️  Note: Your portfolio is not very diversified. Consider adding more stocks.")
        
        largest_stock = max(self.portfolio, key=lambda x: self.portfolio[x] * self.stock_prices[x])
        print(f"🏆 Top Holding: {largest_stock} ({ (self.portfolio[largest_stock]*self.stock_prices[largest_stock]/total_value)*100:.1f}% of portfolio)")
        print("="*60)

    def search_stock(self):
        stock = input("Enter stock symbol to search: ").upper()
        if stock in self.portfolio:
            qty = self.portfolio[stock]
            price = self.stock_prices[stock]
            print(f"\n🔍 Found: {stock}")
            print(f"   Quantity: {qty}")
            print(f"   Current Price: ${price}")
            print(f"   Total Value: ${qty * price:.2f}")
        else:
            print(f"❌ {stock} not found in your portfolio.")

    def show_chart(self):
        if not self.portfolio:
            print("📭 Portfolio is empty.")
            return

        print("\n📈 Portfolio Allocation Chart")
        print("-" * 30)
        for stock, quantity in self.portfolio.items():
            value = quantity * self.stock_prices[stock]
            bars = "█" * int(value // 100) # One block per $100
            print(f"{stock:5} | {bars} (${value:.0f})")

    def clear_portfolio(self):
        confirm = input("⚠️  Are you sure you want to clear EVERYTHING? (y/n): ").lower()
        if confirm == 'y':
            self.portfolio.clear()
            self.save_portfolio(silent=True)
            print("🗑️  Portfolio cleared.")
        else:
            print("Cancelled.")

    def run(self):
        while True:
            print("\n📊 STOCK PORTFOLIO TRACKER")
            print("1. Add Stock")
            print("2. View Portfolio")
            print("3. Search Stock")
            print("4. Show Allocation Chart")
            print("5. Remove Stock")
            print("6. Clear Portfolio")
            print("7. Clear Screen")
            print("8. Exit")

            choice = input("\nSelect an option (1-8): ")

            if choice == "1": self.add_stock()
            elif choice == "2": self.view_portfolio()
            elif choice == "3": self.search_stock()
            elif choice == "4": self.show_chart()
            elif choice == "5": self.remove_stock()
            elif choice == "6": self.clear_portfolio()
            elif choice == "7": self.clear_screen()
            elif choice == "8":
                print("👋 Exiting... Happy investing!")
                break
            else:
                print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    tracker = StockTracker()
    tracker.run()