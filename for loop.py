#for loops = execute a block of code a fixed number of times.
#you  can iterate over a range, string, sequence, etc.

#we can use the same concept of (start, end, step) inside range function.

for counter in range (1, 11, 2):
    print(counter)

print("HAPPY NEW YEAR")


#String iteration using for loop

credit_card = "1234-5678-9012-3456"

for x  in credit_card:
    print(x)

#There are two special keyword we can use both in while loop and for loop. They are continue, break

for x in range (1, 21):
    if x == 13:
        continue
    else:
        print(x)


for x in range (1, 21):
    if x == 13:
        break
    else:
        print(x)
