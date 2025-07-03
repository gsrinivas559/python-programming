# Standards And Naming Conventions --->
# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# each method is treated as a test method
import pytest


# 2 types to run pytest files
# a. using edit configurations and adding pytests --> browse script path and then apply
# b. using terminal --> change directory to the script path till the directory and use py.test
# To see more verbose and additional information metadata while running, use py.test -v
# To see console logs, we need to add -s flag in the command, use py.test -v -s

# to run specific test scripts matching specific text, we can use regular expression
# we have to pass -k flag and the text common in tests in command line

# -m Flag - for running specific tags related test cases
# you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
# you can mark tests with @pytest.mark.xfail for those execution will be done but will not consider result in reports
# datadriven and parameterization can be done with return statements in list form
# When you define scope to class only, it will run once before class is initiated and at the end

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_Greet():
    print("Good Morning!")


@pytest.mark.usefixtures("crossBrowser")
def test_crossBrowser(crossBrowser):
    print(crossBrowser)  # will run 3 times
    print(crossBrowser[1])  # all 1st index values will be retrieved i.e, ChromeDriver EdgeDriver GeckoDriver
