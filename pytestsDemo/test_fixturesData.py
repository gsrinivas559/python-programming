import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_fetchData(self, dataLoad):
        print(type(dataLoad))  # <class 'list'>
        print(dataLoad)  # ['Python', 'Java', 'Javascript']
        print(dataLoad[0])  # Python
