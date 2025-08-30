#INDEXING  =  accessing elements of a sequence using [] (indexing operator)
# [start :  end  : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[2]) #start position of the index
print(credit_number[2: 4])#start to end means 2-4 index number
print(credit_number[:4])#we can omit 0 in start because python takes it automatically
credit_number[5:]#it assumes everything from 5 to everything
credit_number[-5]#we can use negative index also
print(credit_number[::2])#it will print every second character in our string and this is the STEP


