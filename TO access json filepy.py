#TO access json file

import json

employee = {
    "name": "Spongebob",
    "age" : 30,
    "job" : "cook"
}

file_path = "test2.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent= 4) #dump method will convert our dictionary into a json string, indent use to create indentation spaces in json file.
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file is already exists!")
