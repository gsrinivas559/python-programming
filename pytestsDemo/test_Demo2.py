# Standards And Naming Conventions --->
# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# each method is treated as a test method

def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test Failed due to strings mismatch"


def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == b, "Addition do not match"
