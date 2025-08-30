#Magic method  = Dunder methods (double underscore) __init__, __str__, __eq__

#They are automatically called by many of Python's built in operations.

# They allow developers to define or customize the behavior of the object
class Book:
    
    def __init__(self, title, author, num_pages):# used to initialize and if we print the value directly we will get the memory address only
        self.title = title
        self.author = author
        self.author = author
        self.num_pages = num_pages





    def __str__(self):# we use it to directly print the value of the object in the console not the memory address
        return f"{self.title} BY {self.author} " 





    def __eq__(self, other):# EQ MEANS EQUAL, WE CHECK HERE IF TWO OBJECTS ARE EQUAL OR NOT
        return self.title == other.title and self.author == other.author




    def __gt__(self, other):# GT IS GREATER THAN, FOR CHECKING IF THE TWO OBJECT WHICH IS GREATER
        return self.num_pages > other.num_pages



    def __lt__(self, other):# LT IS lesser THAN, FOR CHECKING IF THE TWO OBJECT WHICH IS lesser
        return self.num_pages < other.num_pages



    def __add__(self, other):# for adding two objects
        
        return f"{self.num_pages + other.num_pages} pages"


    def __contains__(self, keyword):# for checking if that is present in the  objects or not
        return keyword in self.title or keyword in self.author




    def __getitem__(self, key):# for getting items  objects
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"




book1 =  Book("The Hobbit", "J.R.R Tolkein", 310)
book1 =  Book("Harry Potter and the Philosopher's Stone", "J.K Rowling", 223)
book1 =  Book("The Lion, the Witch and the Wardrobe", "C.S Lewis", 172)
