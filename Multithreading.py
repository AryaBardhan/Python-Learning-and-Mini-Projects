# Multithreading = Used to perform  multiple tasks concurrently (multitasking)
#    Good for I/O bound tasks like reading files or fetching data from API's
#threading.Thread(target=my_function)

import threading
import time

# When the function is taking arguments we need to use the args  keyword argument in thread
def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking the dog {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")


def get_mail():
    time.sleep(4)
    print("You get the mail")


chore1 = threading.Thread(target=walk_dog, args=("Scoooby"))
chore1.start() #To initiate the task

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()


chore1.join() # we used the join method to wait until the tasks are completed and then print the last print statement
chore2.join()
chore3.join()
print("All chores are completed!!")
