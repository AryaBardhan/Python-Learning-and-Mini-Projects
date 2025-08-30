import json

file_path = "E:/Python/test2.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")



#if we need to access specific data form the file we can use index to access that in the print (content[0]) like that
