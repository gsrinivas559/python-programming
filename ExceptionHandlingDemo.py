# try and except blocks are used to handle the exceptions
# we know some line of code will fail and will stop or halt the execution
# if we want to continue regardless of exception, then we have to put that code in try and except block
# try --> when we know some line of code throws some kind of exception, we have to use try block to handle the exception
# except --> to catch the exception occurred, we use except block where we can print the exception and debug the issues
# raise --> used to create an exception with custom message
# finally --> always executes regardless of failure and not mandatory to use, but only used with try and except block
# two ways exception can be thrown explicitly when condition not matches

itemsAddedToCart = 0
# code to add the items in cart by clicking on the items
# After adding 2 items to cart

# 1. Check condition using conditional statements
if itemsAddedToCart != 2:  # raise Exception("Items count mismatched")
    pass  # does nothing

# 2. Check condition using Assertion
assert (itemsAddedToCart == 0)  # checks the condition is true or not, if it true, then condition is passed
# if condition is false, then throws AssertionError

# Scenario 2: suppose if we want to open the file which is not present in the directory
# We get FileNotFound Exception, to handle the exception we can use try and except blocks
# Without try, except block
# with open('exceptionHandlingDemo.txt', 'r') as reader:
# FileNotFoundError: No such file or directory: 'exceptionHandlingDemo.txt'
#     reader.read()

# Note: Checking negative scenarios using wrong file names to perform the exceptions for all the below scenarios
# using try, except block
try:
    with open('exceptionHandlingDemo.txt', 'r') as reader:
        reader.read()
except:
    print("File Not Found exception occurred")  # File Not Found exception occurred

# to print python exception in except block
try:
    with open('exceptionHandlingDemo.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)  # No such file or directory: 'exceptionHandlingDemo.txt'
finally:
    print("cleaning up resources")
