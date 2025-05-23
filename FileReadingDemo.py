# In Python, files are read using open function
# For reading and writing into file, we need to create a text file
file = open('languages.txt')

# read --> reads all the lines from the file
# print(file.read())  # Python Java Javascript C# Ruby

# read(n) --> n no of characters to fetch from the file
# print(file.read(2))  # Py

# readline --> prints line by line when we use multiple read lines from the file
# print(file.readline())  # Python
# print(file.readline())  # Java

# readlines --> reads all the lines from the file and returns in a list
# print(file.readlines())  # ['Python\n', 'Java\n', 'Javascript\n', 'C#\n', 'Ruby\n']

# to print all the lines in a file line by line, we can use loops
# line = file.readline()
# while line != "":
#     print(line) # ['Python\n', 'Java\n', 'Javascript\n', 'C#\n', 'Ruby\n']
#     line = file.readline()

# using for loop, we can also fetch all the lines from a file
values = file.readlines()
for value in values:
    print(value)  # ['Python\n', 'Java\n', 'Javascript\n', 'C#\n', 'Ruby\n']

# to close the file, we use file.close()
# Always best practices to close the opened files at the end
file.close()
