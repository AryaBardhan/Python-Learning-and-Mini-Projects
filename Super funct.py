# super() = Function used in a child class to call methods from a parent class (superclass).

#         Allow you to extend the functionality of the inherited methods.

class shapes:# the thing are common in all other class and we dont wanna rewrite every time in every class so we can create a constructor in the Parent class to reuse the attributes in it.
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(shapes):
    def __init__(self, color, is_filled , radius):
        super().__init__(color, is_filled) #To use the attributes that are inside the Parent class we can use the super in this format.
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 *self.radius *self.radius}")

class Square(shapes):
    def __init__(self, color, is_filled , width):
        super().__init__(color, is_filled) #To use the attributes that are inside the Parent class we can use the super in this format.
        self.width = width

class Triangle(shapes):
    def __init__(self, color, is_filled , height, width):
        super().__init__(color, is_filled) #To use the attributes that are inside the Parent class we can use the super in this format.
        self.width = width
        self.height = height


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="Green", is_filled=False, width=5)
triangle = Triangle(color="Blue", is_filled=True, height=5, width= 6)

print(circle.color)
print(circle.is_filled)
print(f"{circle.is_filled}")

print(square.color)
print(square.is_filled)
print(f"{square.is_filled}")

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.is_filled}")

circle.describe()
