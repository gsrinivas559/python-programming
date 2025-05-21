# 2. While Loop --> Another way of looping through the statements based on condition whereas for loop depends on range
# Jumping Statements --> Continue, Break
# Continue --> skips the current iteration
# Break --> halts the looping and comes out of the loop

# program to print 10 numbers using while loop
i = 10
while i > 0:
    if i == 9:
        i = i - 1
        continue
    if i == 3:
        break
    print(i)  # 10, 8, 7, 6, 5, 4
    i = i - 1
print("Code execution completed")
