# fixtures are used as setup and tear down methods for test cases - conftest to generalize fixture content
# conftest - we can add the content which is need to run for all the test cases
# class name should start with Test

import pytest


@pytest.mark.usefixtures("setup")
class TestFixtureExample:

    def test_fixtureDemo(self):
        print("I will be executing steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will be executing steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will be executing steps in fixtureDemo2  method")

    def test_fixtureDemo3(self):
        print("I will be executing steps in fixtureDemo3 method")
