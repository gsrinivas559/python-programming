# DataTypes -->
# 1. Numeric --> int, float, long[deprecated in python3.x], complex
# All numbers are considered under numeric data type

# create a variable with integer value.
a = 100
print("The type of variable having value", a, " is ", type(a))

# create a variable with float value.
b = 10.2345
print("The type of variable having value", b, " is ", type(b))

# create a variable with complex value.
c = 100 + 3j
print("The type of variable having value", c, " is ", type(c))

# 2. String -->  sequence of characters represented by either single or double-quotes
a = "string in a double quote"
b = 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a, "concatenated with", b)

# using '+' to concate the two or several strings
print(a + " concated with " + b)
