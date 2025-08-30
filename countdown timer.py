# import time
# time.sleep(3)
# print("TIME'S UP")

#Count forward

# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)
    

# print("TIME'S UP")


#ANother technique (whuch is count backwards)

# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     print(x)
#     time.sleep(1)
    

# print("TIME'S UP")


import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x%60
    minutes = int(x/60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    

print("TIME'S UP")
