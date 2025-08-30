#validate user input exercise 
# 1. username is no more than 12 characters
# 2. username must not contain spaces 
# 3. username must not contain digits

username = input ("Enter the username: ")

# username.find("") is used for finding anythiing inside the inverted comma
# username.isalpa() is used for checking alphabets present there or not
# And we cant use elif not to uset this string methods to use reversely

if len(username) > 12:
  print("Your username can't be more than 12 characters ")
elif not username.find(" ") == -1:
  print("your username cant contain spaces")
elif not username.isalpha():
  print("your username cant contain numbers")
else:
  print(f"Welcome {username}")