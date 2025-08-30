# class variable =  Shared among all instances of a class 
#                     Defined outside the constructor
#                     Allow you to share data among all objects created 
#                     from that class


class Student:
    
    class_year = 2024 #This is a class variable which is outside the constructor and can accessed within the class
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student("Arya", 30)
student2 = Student("Patric", 35)

print(student1.name)
print(student2.age)
print(student2.class_year)
print(Student.class_year) #it is good practice to access the class variable with the classname other than any other object inside the class which helps to improve readability not other instance variable in the class here student1 is object/instance variable
