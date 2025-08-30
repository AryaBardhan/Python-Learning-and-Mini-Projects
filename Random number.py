import random

# number = random.randint(1, 6)

# print (number)



low =  1
high =  100
number = random.randint(low, high)
print(number)


#for random floating point number
number = random.random()
print(number)


#we can choose a random choice from some options in a tuple, list, set

options = ("rock", "paper", "scissors")

option = random.choice(options)
print(option)


#We also  have shuffle keyword in random
cards = ["2","3", "4", "5"]
random.shuffle(cards)
