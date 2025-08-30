#to edit csv file

import json

import csv

employee = [["Name", "Age", "Job"],
            ["Sponge", 30, "cook"],
            ["Joe", 27, "Scientist"],
            ["Harry", 14, "Unemployed"]]

file_path = "test2.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file) #writer is a method of this module, it is object  it provides methods providing data to a csv file
        for row in employee:
            writer.writerow(row)# it also given a new line after every iteration so to prevent that we use keyword argument of newline= ""
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file is already exists!")
