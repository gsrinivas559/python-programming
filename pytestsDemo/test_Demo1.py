# Standards And Naming Conventions --->
# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# each method is treated as a test method

# 2 types to run pytest files
# a. using edit configurations and adding pytests --> browse script path and then apply
# b. using terminal --> change directory to the script path till the directory and use py.test
# To see more verbose and additional information metadata while running, use py.test -v
# To see console logs, we need to add -s flag in the command, use py.test -v -s

# to run specific test scripts matching specific text, we can use regular expression
# we have to pass -k flag and the text common in tests in command line

def test_firstProgram():
    print("Hello")


def test_Greet():
    print("Good Morning!")
