# Polymorphism =  Greek word that means to "have many forms or faces"
#                 poly = Many
#                 Morphe = Form
                
#                 TWO WAYS TO ACHIEVE Polymorphism
                
#                 1.Inheritance = An Object could be treated of the same type as a parent class
#                 2. "Duck Typing" = Object must have necessary Attributes /methods

from abc import ABC, abstractmethod #to use abstract class we need to import it 
class Shape:
    @abstractmethod #it is a decorator for abstract method
    def area(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def  area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base *self.height *0.5

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius) #we call the super constructor to use the radius attribute from the parent class 
        self.topping = topping 

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepproni", 15)]

for shape in shapes:
    print(f"{shape.area()}cm^2")
