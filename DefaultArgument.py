# default arguments =  A default value for a certain parameters 
#                     default is used when the arguments is omitted
#                     make your function more flexible, reduces 
#                     # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword 4.arbitary




#DEFAULT ARGUMENTS
def net_price(list_price, discount=0, tax= 0.04):
    return list_price* (1-discount) * (1+tax)

print(net_price(500))# we are only passing argument for list_price other is set a default value at first.


import time
def count(start, end):
    for x in range (start, end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)


# #Keyword Arguments =  an argument preceded by an identifier
#                         helps with readability
#                         order of arguments doesn't matter

def hello (gretting, title, first, last):
    print(f"{gretting} {title}{first}{last}")

hello("Hello", title ="Mr.", last="Squarepants", first="Spongebob") #It is keyword argument where we assigning the value at the time of calling and here the order doesnt matter.


# NOTE: positional argument("Hello" in here) should be at first
