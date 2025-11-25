price = (120,80,150,200,90)

total_price = sum(price)
print("Total Price:", total_price)
print(max(price))
print(min(price))
expensive_items = [p for p in price if p > 100]
print("Expensive Items:", expensive_items)
price += (110,)
print("Updated Prices:", price)