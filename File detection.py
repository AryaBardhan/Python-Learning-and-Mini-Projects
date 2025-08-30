import os # this module helps python to interact with the operating system

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists!")
    if os.path.isfile(file_path):
        print("That a file")
    elif os.path.isdir(file_path): #here .path, isdir are built in methods in python where path checks for the file path and the isdir checks for is this a directory or not, and file_path is the argument here that we pass
        
        print("That is a directory")
else:
    print("The location doesn't exists")
