#Python writing files (.txt, .json, .csv)

txt_data =  "I like Pizza!"

file_path = "test1.txt" #we can set our custom path here also, like relative or absolute path 

'''
with open (file_path, "w") as file: 


# to create a file we have to write this, where with is a statement which is used to wrap a block to execute, it automatically close the file after running so  it is not necessary to close it manually, open is used to open the file from file_path and "w" is used for writing format,  return a file object with 2 parameters file_path and mode, as is used to name the object as file.
    
    
    #NOTE: here w is for writing mode, x for creating the file if not exists
    
    
    file.write(txt_data)
    print(f"txt_file '{file_path} is created")
    
    
'''


'''
try:
    with open (file_path, "w") as file:
        file.write(txt_data)
        print(f"txt_file '{file_path} is created")
        
        
except FileExistsError:
    print("That file already exists.")

'''

try:
    with open (file_path, "a") as file: # a is used for append
        file.write("\n" + txt_data)
        print(f"txt_file '{file_path} is created")
        
        
except FileExistsError:
    print("That file already exists.")
