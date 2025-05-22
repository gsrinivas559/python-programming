# Inheritance __> Acquiring parent properties into child class
from OopsDemo import Calculator # syntax to import a class from file


class ChildClass(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.getSummation()


obj = ChildClass()
print(obj.getCompleteData())  # here getSummation will throw error due to the parameters not initialized through
# constructor for Calculator class, in the child class we have to initialize parent constructor to pass the
# parameters to the calculator constructor
#After adding the constructor, Now will give the required results
