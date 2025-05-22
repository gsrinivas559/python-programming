# Strings --> sequence of characters combined into variables
# Strings are declared in single quotes or double quotes
# Strings have many in-built functions which are used while performing tasks
email = "test123@gmail.com"
name = "test123"
print(email)  # test123@gmail.com
print(email[1])  # prints 1st character in string --> e
print(email[0:7])  # test123 --> prints substring of a string [using slicing]
print(name in email)  # True --> return true when the another string is present in main string [substring check]
print("The "+name+" is present in "+email)  # The test123 is present in test123@gmail.com --> Concatenation using '+'
var = email.split("@")
print(var)  # ['test123', 'gmail.com'] --> split function
stringWithSpaces = " stringWithSpaces "
print(stringWithSpaces.strip())  # 'stringWithSpaces' --> trim function in python, we use strip function
print(stringWithSpaces.lstrip())    # 'stringWithSpaces '  --> lstrip function - trimming left side of string
print(stringWithSpaces.rstrip())    # ' stringWithSpaces'  --> rstrip function - trimming right side of string
