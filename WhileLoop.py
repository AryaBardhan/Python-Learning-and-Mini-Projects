#while loop = execute some code WHILE some condition remains True

name = input("Enter Your name: ")

#at first we are using if else but if we want to continue user to type their name, we could not do that until they typing something
#we use while loop here to continously print until the user type their name, means until the while loops condition is true, the name = input() will be prompted continuosly
#while the condition in while loop is true repeat the piece of code forever
#To escape infinite loop we need to provide a way for user to skip that so we provided the name = input( ) inside the while loop otherwise it will run infinitely but if the user enter their name then the program will stop

while name ==  "":
  print("You did not enter your name")
  name = input("Enter your name: ")

print(f"Hello {name}")



