orders = []
quantity = None

menu = {
    'Pizza': 12.99,
    'Burger': 8.99,
    'Pasta': 10.99,
    'Salad': 6.99,
    'Soda': 1.99
}

while True:
    print("\n----- Menu -----")
    for dish, price in menu.items():
        print(f"{dish}: ${price}")
    print("\n----------------")

    order_item = input("Enter the dish you want to order ('Done' to Make Bill): ").capitalize()
    
    if order_item in menu:
        quantity = int(input(f"How many {order_item}s would you like to order? "))
        orders.append((order_item, quantity))
    elif order_item == 'Done':
        break
    else:
        print("Sorry, that item is not on the menu. Please choose from the available options.")

# calculate Total
# Receipt Printing
print("\n----- Receipt -----")
total = 0
for item, quantity in orders:
    total += menu.get(item) * quantity
    print(f"{item} x{quantity}: ${menu[item] * quantity:.2f}")

print(f"Total: ${total:.2f}")
print("-------------------")