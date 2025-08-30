class Student:
    
    num_students = 0
    class_year = 2024 
    
    # within our contructor we can write any code,we can replace self with the class name itself
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        Student.num_students += 1 
        
student1 = Student("Arya", 30)
student2 = Student("Patric", 35)

print(student1.name)
print(student2.age)
print(student2.class_year)
print(Student.class_year)

print (f"My graduating class of {Student.class_year} has {Student.num_students} students")

print(student1)
print(student2)
