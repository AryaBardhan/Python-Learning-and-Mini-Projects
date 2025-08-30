#Static methods = A method that belong to a class rather than any object from that class(Instance)
#Usually used for general utility functions

#Instance Method =  Best for operations on instances of the class(objects)

#Static method =  Best for utility functions that do not need access to class data


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    
    @staticmethod
    def is_valid_position(position): #in static method we dont have ant self as first arguments, we dont work with the object created from this class
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor "]
        return position in valid_positions

# we dont need to write like to use static
# employee1 = Employee()  

employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squid", "Cashier") 
employee3 = Employee("Spongebob", "Cook") 


print(Employee.is_valid_position("Rocket Scientist")) # to use the static method we the name of the class Employee
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


#With the static method we only need access the class we dont need create a object from that class
