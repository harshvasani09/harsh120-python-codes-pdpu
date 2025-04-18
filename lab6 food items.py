menu = [
    ("Paneer Butter Masala", 250),
    ("Chicken Biryani", 220),
    ("Masala Dosa", 100),
    ("Chole Bhature", 120),
    ("Gulab Jamun", 60),
    ("Butter Naan", 40)
]

sorted_menu = sorted(menu, key=lambda item: item[1], reverse=True)

print("Menu sorted by price (high to low):")
for food, price in sorted_menu:
    print(f"{food}: ₹{price}")
