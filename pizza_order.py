print("Welcome to Pizza Order.com!")
order = input("Order the size of the pizza (S, M, L): ")
add_pepperoni = input("Do you want to add pepperoni? (Y/N): ")
add_cheese = input("Do you want to add extra cheese? (Y/N): ")
bill = 0

if order.lower() == "s":
    bill += 15
    print(f"You ordered a small size pizza: ${bill}")
elif order.lower() == "m":
    bill += 20
    print(f"You ordered a medium size pizza: ${bill}")
else:
    bill += 25
    print(f"You ordered a large size pizza: ${bill}")

if add_pepperoni.lower() == "y":
    if order.lower() == "s":
        bill += 2
    else:
        bill += 3

if add_cheese.lower() == "y":
    bill += 1

print(f"Your final bill is: ${bill}")
print("Thank you for your order!")
