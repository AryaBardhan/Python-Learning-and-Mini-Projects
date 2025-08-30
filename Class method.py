#Class methods = Allow operations related to the class itself
                # Take (cls) as the first parameter, which represents the class itself.
                
# Class method = best for class-level data or require access to the class itself 

# Static method = best for utility functions that do not need access to class data

#Instance method = Best for operations on instance of the class (objects)

class Student:

    count = 0
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

        
        #Instance method
    def get_info(self):
        return f"{self.name} {self.gpa}"

        
    @classmethod
    def get_count(cls):
        return f"Total # of students:  {cls.count}"
    
    
student1 = Student("Arya", 3.2)
student1 = Student("niche", 2.0)
student1 = Student("ola", 4.0)


print(Student.get_count())
