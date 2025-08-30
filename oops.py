# object  = A "bundle" of related attributes (variables) and methods (function) 

# Ex. phone, cup, book
# You need a "class" to create many objects


# class = (blueprint) used to design the structure and layout of an object
class Car:
    def __init__(self, model, year, color, for_sale): #it is a constructor which helps to create an object. It is a dunder method, dunder means double underscore. we need this methosd to create object and self means this object creating right now and this method is acts as a function. self, model, color, for_sale this are the attributes 
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

car1 = Car("pagani", 2024, "Green", False)

#if we print the car1 only it will give the memory address only

print(car1.model)#the . in this is known as attribute access operator  


#In simple terms methods are the functions inside the class like 
# def drive(self):. def rotate(self):
