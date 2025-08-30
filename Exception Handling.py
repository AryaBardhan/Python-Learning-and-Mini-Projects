# exception =  An event that interupts the flow of a program 
#                 (ZeroDivisionError, TypeError, ValueError)
#                 1.try, 2. except, 3. finally


# when we try to divide 1 / 0 then we ZeroDivisionError

#when we try to add one int and other string value we get type error like this ex.- 1 + "1"  


#when we try to typecast a value of wrong datatype we get ValueError
# for ex.- int ("pizza ")

#finally block always runs regardless there is any exception or not

# Syntax for try, except, finally

'''
try:
    #Try some code
except:
    #Handle an Exception
finally:
    #Do some clean up
    
'''
try: 
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You cant divide by Zero Idiot")
except ValueError:
    print("Enter only numbers please!")
except Exception: 
    print("All exceptions are accepted")# this accepts all exception but it is a bad practice and a broad way to accept exceptions.
finally:
    print("Do some clean up here")
