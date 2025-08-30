# *args = allow you to pass multiple non-key arguments. args means arguments
# **kwargs =  allows you to pass multiple keyword-arguments. keyword argument is kwargs
#                     *  <-- unpacking operator



#we could modify the argument so it could take more positional arguments in it. 
#By using the unpacking operator * we make them in a tuple so that we can take more

#we can change the name args to something else also but the operator is mainly important

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3))  

#kwargs is nothing just a dictionary same as args where it is tuple

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

print_address(street="123.Fake street", city="Kolkata", state="West Bengal", zip="700061" )
