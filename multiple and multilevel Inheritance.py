# multiple inheritance = inherit from more than one parent class
#                         C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent

#                         C(B) <= B(A) <= A



class Animal:
    
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Prey(Animal):# multilevel inheritance from animal class
    def flee (self):
        print("This animal is fleeing")

class Predator(Animal):# multilevel inheritance from animal class
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):# Inheritance
    pass

class Hawk(Predator):# Inheritance
    pass

class Fish(Prey, Predator): #multiple inheritance
    pass

#objects

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

hawk.hunt()
