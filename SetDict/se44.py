products = {
    "Laptop": 15,
    "Mouse": 5,
    "Keyboard": 8,
    "Monitor": 12,
    "Headphones": 6
}

print("Products with quantity less than 10:")

for product, quantity in products.items():
    if quantity < 10:
        print(product, ":", quantity)