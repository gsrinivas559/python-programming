# 3. List --> The list in Python is it can simultaneously hold different types of data.
# Formally list is an ordered sequence of some data written using square brackets([]) and commas(,).
# list of having only integers
a = [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3, 4, 5, 6]

# list of having only strings
b = ["hello", "john", "reese"]
print(b)  # ['hello', 'john', 'reese']

# list of having both integers and strings
c = ["hey", "you", 1, 2, 3, "go"]
print(c)  # ['hey', 'you', 1, 2, 3, 'go']

# index are 0 based. this will print a single character
print(c[1])  # this will print "you" in list c
print(c[-1])  # this will print "go" in list c and to fetch last index, we use -1
print(c[1:3])  # this will print "you, 1" in list c and slicing is used to fetch values between the index's

# insertion can be possible by specifying the index
c.insert(2, "Numbers")
print(c)  # ['hey', 'you', 'Numbers', 1, 2, 3, 'go']

# appending to the list adds the element at the end of the array
c.append("End")
print(c)  # ['hey', 'you', 'Numbers', 1, 2, 3, 'go', 'End']

# Updating the index is possible
c[2] = "Numeric Data"
print(c)  # ['hey', 'you', 'Numeric Data', 1, 2, 3, 'go', 'End']

# Del is used to delete the specific index value
del c[2]
print(c)  # ['hey', 'you', 'Numeric Data', 1, 2, 3, 'go', 'End']

# 4. Tuple --> sequence of data similar to a list. But it is immutable means write-protected and cannot be updated
# Data in a tuple is written using parenthesis and commas.
# tuple having only integer type of data.
# index of tuples are also 0 based.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple type of data.
b = ("hello", 1, 2, 3, "go")
print(b)  # prints the whole tuple

sentence = ("My", "name", "is", "Srinivas")
# Updating the index is not possible
# sentence[3] = "Vasu" # TypeError: 'tuple' object does not support item assignment
print(sentence)  # ('My', 'name', 'is', 'Srinivas')
