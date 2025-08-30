# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#   print(f"you like {food}")
#   food = input("enter another food you like (q to quit): ")

# print ("bye")



num = int(input("Enter a # between 1-10: "))
while num < 1 or num > 10:
  print(f"{num} is not valid")
  num = int(input("Enter a # between 1-10: "))

print ( f"Your number is {num}")
