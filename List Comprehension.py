# List Comprehension = A Concise way to create lists in python 
#                             Compact and easier to read than traditional loops
#                    formula:-[expression for value in iterable if condition]

#Traditional way
doubles = []
for x in range (1, 11):
    doubles.append(x * 2)

print(doubles)

#list comprehension

doubles = [x * 2 for x in range(1, 11)]
print(doubles)
