# Decorator = A function that extends the behaviour of anotther funtion w/o modifying the base function

#                 Pass the base function as an argument to the Decorator

                
                
#                 @add_sprinkles
#                 get_ice_cream("vanilla")


# We are addiing to the base function without modifying it ,is the fucntion of decorators


#syntax of creating a decorator function
def add_sprinkles(func):
    def wrapper():                  # It is necessary to a nested function inside the decorator function because we only to execute the code when want sprinkles on ice-cream not by wherever calling the decorator class only.
        print("*You add sprinkles 🎊*")
        func()
    return wrapper


@add_sprinkles 
def get_ice_cream():
    print("Here is your ice cream 🍨")

get_ice_cream()
