#Shopping Cart Program: To help you keep count of the
# total money your spending on your grocery items.

foods = []
prices = []
total = 0

while True:
    print("1) Add item")
    print("2) Show cart & Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 2:
        break
    
    item = input("Enter a Grocery Item (q to quit): ")
    if item.lower() == "q":
        continue
        
    price = float(input(f"Enter the Price of {item}: $"))
    foods.append(item)
    prices.append(price)

print("--------CART TOTAL-------")
for item, price in zip(foods, prices):
    print(f"{item}: ${price}")
total = sum(prices)
print(f"Your total is ${total}")

