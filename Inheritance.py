# Inheritance = Allow a class to inherit attributes and methods from another class 

# Helps with code reusability and extensibility
# class Child(Parent)
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
        def eat(self):
            print(f"{self.name} is eating")

        def sleep(self):
            print(f"{self.name} is sleeping")


#the dog class with inherit all the attributes and methods from the parent class Animal
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
