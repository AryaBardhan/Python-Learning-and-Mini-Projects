#function =  A block of reusable code place () after the function name to invoke it

def happy_birthday(name):
    print(f"Happy Birthday to {name}")
    print("you are old!")
    print()

    
#to invoke this function we type the function name and a set of parenthesis
#if we want to call this 3 times we need to type 3 times

happy_birthday("Joe")
happy_birthday("Steve")
happy_birthday("BRO")
# With function we can send a data directly to a function 

# Any data you send to the function is called Arguments which we can write inside the parenthesis while calling

# And we need to add a parameter inside the parenthesis of the actual function which acts as a temporary variable.


#  Here "name" is a parameter and "BRO" is an argument. 


#RETURN Statement = statement used to end a function and send a result back to the caller

def add (x, y):
    z = x+y
    return z

def divide(x, y):
    z = x/y
    return z
def substract(x, y):
    z = x-y
    return z
def multiply(x, y):
    z = x*y
    return z

print(add(1, 2))
print(divide(1, 2))
print(substract(1, 2))
print(multiply(1, 2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("arya","bardhan")

print(full_name)
