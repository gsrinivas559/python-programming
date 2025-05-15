# In Python, No need to decare a type for the variables explicitly

# To find the datatypes of the variables
a, b, c, d, e = 5, 6.5, 's', "Hello", True
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'str'>
print(type(e))  # <class 'bool'>

# throws type error when try to concatenate wih str with int
# print("A value is: " + a)  # TypeError: can only concatenate str (not "int") to str
# To resolve the above issue, we can concatenate the values using format method
print("{} {}".format("A value is: ", a))
