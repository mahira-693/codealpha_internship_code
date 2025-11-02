stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "MSFT": 300}

portfolio = {}
total = 0

print("💹 Stock Portfolio Tracker")

while True:
    stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = qty
    else:
        print("⚠️ Stock not found in price list!")

# Calculate total value
for stock, qty in portfolio.items():
    total += stock_prices[stock] * qty

print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    print(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}")

print(f"\n💰 Total Investment Value: ${total}")

# Optional: save to file
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
    f.write(f"\nTotal Investment: ${total}")
print("\n✅ Saved to 'portfolio.txt'")
