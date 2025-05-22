# oops --> contains classes, objects, inheritance, constructor, etc.
# classes contains variables and methods
# The functions declared inside the class are called class methods
# functions declared outside the class are called functions
# constructor is used to initialize variables and default constructor is automatically called when an object is created
# constructor name should be __init__
# Variables types -->
# class variables[which are declared inside the class],
# instance variables[which are declared inside constructor and class methods],
# global variables[Which are declared outside the class]
# In Python, new keyword is not needed to create an object
# self keyword is mandatory for calling variables names into method
# self indicates the class and can be referred inside the class when it is needed instead of calling class name
class Calculator:
    num = 100  # class variables

    def __init__(self, a, b):  # parameterized constructor
        self.firstNum = a  # instance variables
        self.secondNum = b
        print("I am automatically invoked when an object is created")

    def getData(self):
        print("I am executing as a method in class")

    def getSummation(self):  # parameterized method
        return self.firstNum + self.secondNum + Calculator.num


obj = Calculator(2, 3)  # syntax to create object
obj.getData()
print(obj.getSummation())

obj1 = Calculator(4, 5)  # syntax to create object
obj1.getData()
print(obj1.getSummation())
