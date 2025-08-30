#dictionary = a collection of {key:value} pairs
#ordered and changeable. No duplicates

capitals = {"USA" : "Washington D.C",
            "India": "New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}


#to get the value associated with USA we use "get" keyword
print(capitals.get("USA"))

#check to see if a key within a dictionary 
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exists")

#TO update a dictionary

capitals.update({"Germany": "Berlin"}) # new updated data
capitals.update({"USA": "Detroit"}) # old updated data

#to remove a key value pair in a dictionary
capitals.pop("China")

# to remove the latest key value pair inserted 
capitals.popitem()

#clear the dictionary
capitals.clear()

#to print only the keys from a dictionary
keys = capitals.keys()# keys is an object which resembles a list.
print(keys)

#to iterate every key of a dictionary
for key in capitals.keys():
    print(key)

#to print all the values in the dictionary


values =  capitals.values()
for value in capitals.values():
    print(value)

#items resembles a 2d list of tuples

items = capitals.items ()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")
