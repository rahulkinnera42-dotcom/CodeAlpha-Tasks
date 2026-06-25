stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 330
}

total = 0

for stock in stocks:
    qty = int(input(f"Enter quantity of {stock}: "))
    total += qty * stocks[stock]

print("\nTotal Investment Value = $", total)