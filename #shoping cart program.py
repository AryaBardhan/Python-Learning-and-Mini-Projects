#shoping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to Quit): ")
    if food.lower()  == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: Rs."))
        foods.append(food)
        prices.append(price)
    
    
print("-----YOUR CART -----")


for food in foods:
    print(food, end= " ")


for price in prices:
    total += price
# The `print()` function is used to display output to the console. In this specific code snippet,
# `print()` is used to display the items in the shopping cart and the total price to the user.
print()
print(f"Your total is: Rs.{total}")
