# In Python, function is a group of related statements that perform a specific task
# def keyword is used as identifier for function
# Declaration
def greetMe():
    print("Good Morning!")


# parameterized function
def greetMeByName(name):
    print("Good Morning! " + name)


def addTwoNumbers(a, b):
    return a + b


# Function call
greetMe()
# parameterized function call
greetMeByName("Srinivas")
print(addTwoNumbers(2, 3))
