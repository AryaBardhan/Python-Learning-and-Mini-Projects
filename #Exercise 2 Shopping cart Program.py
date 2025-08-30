#Exercise 2 Shopping cart Program 

item = input("What item would you like to buy?: ")
price = float (input("What is the price?: "))

quantity = int(input("How many would you like ?: "))
total = price * quantity

# for any placeholder we use this =>  {}

print(f"You have bought {quantity} x {item}/s")
print(f"You have bought ${total}")


