import pytest


# yield - runs after all the test cases like tear down method
# scope="class" - will run once before the tests in class, run all the test cases then run once after the tests in class

@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("Programming languages are created")
    return ["Python", "Java", "Javascript"]


@pytest.fixture(params=[("Chrome", "ChromeDriver"), ("Edge", "EdgeDriver"), ("Firefox", "GeckoDriver")])
def crossBrowser(request):
    return request.param
