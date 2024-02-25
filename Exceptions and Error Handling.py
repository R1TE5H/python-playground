# Exceptions and Error Handling 

# Whenever an Error is logged the Type of Error and Specifics are Shown
    # When a number is divided by zero: ZeroDivisonError: division by zero
# The Error causes the program to end --> Avoid using Try/Exception Blocks

def exists(filename):
    try:                        # Will Try a Block of Code
        f = open(filename)
        f.close()
        print("Found it")
        return True
    except:                     # If an Error Occurs Do X
        print("There is no file named", filename)
        return False
    finally:                    # Regardless of What Happens Do Y
        print("The entire function is complete")
# Program asks for a file and checks to see if the file exists
    # If it does it will print that we found it
    # If it does not it wil print that there is no file

#-----------------------------------------------------------------------------------------------

# Raising our Own Excepitons
    # Instead of letting the code throw an Error we can make it automatically raise and exception
    # This lets the code run but will keep giving internal errors until a Try-Except Block is found
        # Once it is the error is handled and the function will fix itself 
def getAge():
    age = int(input("Please Enter You Age: "))
    if age < 0:
        myError = ValueError("{0} is not a valid age".format(age))
        raise myError
    return age
# Program will ask for a age (number) and will test to see if it is less than 0
    # If it is it will raise/output an error saying "{age} is not a valid age"
    # If it is not it will just return the age
# NOTE:
    # myError = ValueError("{0} is not a valid age".format(age))
    #  raise myError
    # Usually Simplified to:
        # raise ValueError("{0} is not a valid age".format(age))
        
#----------------------------------------------------------------------------------------------

# Handling Infinite Recursion

def recursionDepth(number):
    print("{0}, ".format(number), end="")
    recursionDepth(number +1)
    
# Above will result in an Infinite Recursion
# Below will run the recursion but will stop it once an error is thrown without killing the program

def revisedRecursionDepth(number):
    print("Recursion depth number", number)
    try:
        recursionDepth(number +1)
    except:
        print("I cannot go any deeper into the wormhole")
    
#------------------------------------------------------------------------------------------------

# Checking for Specific Errors
    # Keep Try Block as Small as Possible --> Easier to see what is causing Error
def specificErrors():
    try: 
        num = int(input("Enter a Number: "))
        den = int(input("Enter a Number: "))  
        quotient = num / den
        print(quotient)
    except ZeroDivisionError:
        print("Looks Like You Tried to Divide by Zero")
    except ValueError:
        print("Please Enter a Number")
    finally:
        print("Program Complete")
#------------------------------------------------------------------------------------------------

# Practice
def readPosInt():
    try:
        num = int(input("Please Enter a Positive Number: "))
        if (num > 0):
            print(num, "is a positive number")
        else: 
            print(num, "is not a positive number")
    except ValueError:
        print("It Looks Like you Did Not Input a Number. Try Again")
        readPosInt()
    except KeyboardInterrupt:
        print("\n""Looks like you stopped the dialog")

readPosInt()