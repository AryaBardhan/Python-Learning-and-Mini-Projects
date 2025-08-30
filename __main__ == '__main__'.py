    # if __name__ == __main__: (this script can be imported OR run standalone)

# Functions and classes in this module can be reused without the main block of code executing

def main():
    #Your program goes here
    
#__ can be called dunder

if __name__ == '__main__':
    main()
    
#if we want to just run the piece of code means the functions for example then we can use this if __name__ == '__main__', when we dont wanna run this code in other file but we are importing this file into other file

#sometimes we wanna borrow something other file but dont wanna run the main body so we use that.

#Good practice (code is modular,
# helps readability
# leaves no global variables,
# avoid unintended execution)

#Ex. Library = import library for functionality 
#When running library directly, display a help page


#This is used to make the piece of code importable.
