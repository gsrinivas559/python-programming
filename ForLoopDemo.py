# Loops can be used to iterate through the specific statements performing the required actions
# Loops --> for loop, while loop
# 1. For Loop
# creating the list and iterate through the values in the list
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)

# program to print 5 natural numbers
print("-----*print 5 natural numbers*------")
for j in range(1, 6):
    print(j)

print("------***print sum of first 5 numbers***---------")
# program to print sum of first 5 numbers --> 1 + 2 + 3 + 4 + 5 = 15
summation = 0
for k in range(1, 6):
    summation = summation + k
print("sum of first 5 numbers: ", summation)

# to do multiple increments in the loop, we need to add how many increments needed in the range function
print("-----*print 10 natural number by incrementing 2 values*------")
for m in range(1, 11, 2):
    print(m)

# if we want to skip first index in range, then we have to give only how many we need -->
# range(n) --> till n-1 the values will be printed
print("-----*print 0 to 10 natural numbers*------")
for n in range(11):
    print(n)
