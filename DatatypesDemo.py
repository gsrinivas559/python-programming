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
print("{} {}".format("A value is: ", a))    # A value is:  5

# DataTypes -->
# 1. Numeric --> int, float, long[deprecated in python3.x], complex
# 2. String -->  sequence of characters represented by either single or double-quotes
# 3. List --> The list in Python is it can simultaneously hold different types of data.
# 4. Tuple --> sequence of data similar to a list. But it is immutable means write-protected and cannot be updated
# 5. Dictionary --> unordered sequence of data of key-value pair form and similar to the hash table type.
