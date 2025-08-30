#collection = single "variable" used to store multiple values
#List =  [] ordered and changeable. Duplicate ok.
#set = {} unordered and immutable, but Add/ Remove OK. NO Duplicates.
#Tuple = () ordered and unchangeable. Duplicates Ok. Faster.



#=========================L I S T===========================

# fruits =  ["apple","orange", "banana","coconut" ]
# print(fruits[:3])# to access element in the list we can use indexes


# fruits =  ["apple","orange", "banana","coconut" ]
# for fruit in fruits:
#     print(fruit)

#Methods used in collection
fruits =  ["apple","orange", "banana","coconut" ]
# print(dir(fruits))
# print(help(fruits))


print("pineapple" in fruits) # we can use in operator to find if a value within a list

fruits[0] = "pineapple" #using index we can assign values to that index in the list


fruits.append("pineapple") #append used to add the element at the end of the list.

#to remove an element
fruits.remove("apple")

#to insert an element at an index
fruits.insert(0, "pineapple")

#to sort elements in the list like in alphabetical order
fruits.sort()

#to reverse the list
fruits.reverse() # if we want to reverse in alphabetical order we need to sort first then we can use reverse function

#to clear the list
fruits.clear()

#we can return the index of an element of the list
print(fruits.index("pineapple"))

#count duplicates in the list

print(fruits.count("banana"))
print(fruits)


#=========================== S E T ========================== 

#to display all the different attributes, and method we use the dir function

#to display the details of the attributes and method we use help function

fruits = {"apple", "orange", "banana", "coconut"} #the output will be in unordered format

#to add 

fruits.add("pineapple")

#to remove
fruits.remove("apple")

#to pop element means to remove the first element in the set though it is random

fruits.pop()


#to clear 

fruits.clear()


#SETS WORK BETTER WHEN WE ARE USING CONSTANTS. MEANS WE DONT WANT ANY DUPLICATES.


#=========================== T U P L E ======================


fruits = ("apple", "orange", "banana", "coconut")


#to check whether the element is present inside the tuple 

print("pineapple" in fruits)

#to count duplicates or occurence of an element in the tuple

fruits.count()

#to find the index position for an element in the tuple we use

print(fruits.index("apple"))


#Tuples are also iterable so we can use for loop 
