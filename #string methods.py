#string methods
name = input("Enter your full Name: ")
phone_number = input("Enter your number: ")
# result =len(name)

result = name.find("a") #helps finds the first occurrence of the letter or word or anything 
result = name.rfind("q") #helps finds the last occurrence of the letter or word or anything 
result = name.capitalize()# capitalize just the first letter
result = name.upper()# for all characters uppercase
result = name.lower()# for all characters in lowercase
result = name.isdigit()#it only returns true if the string contains a digit
result = name.isalpha()#it only returns true if the string contains only alphabetical character
result = phone_number.count("-")#count how many character are there in  the string
result = phone_number.replace("-", " ")#replace the another character with empty string or anything

print(help(str)) #by the line we can get all information about string available in python
print(result)