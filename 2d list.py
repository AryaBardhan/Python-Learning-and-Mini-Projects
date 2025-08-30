# a 2d list which is made up of other lists


# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# print(groceries[2][1]) # this is like coordinates like rows and columns in matrix


#for actual 2d list we can use it like this

groceries = [["apple", "orange", "banana", "coconut"],      ["celery", "carrots", "potatoes"],["chicken", "fish", "turkey"]]


for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()


# we can put tuples under list like ([], [], []), we can  put list under tuples [(), (), ()], we can put sets also like this
