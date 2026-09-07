products = {
    "Laptop": 50000,
    "Mouse": 800,
    "Mobile": 20000,
    "Keyboard": 1200,
    "Headphones": 1500
}

print("Products above ₹1,000:")

for product, price in products.items():
    if price > 1000:
        print(product, ":", price)