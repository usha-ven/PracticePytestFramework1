import pytest

@pytest.yield_fixture()
def setUp():
    print("This is login by email test")
    yield
    print("Close browser after login")


def test_LoginByFacebook(setUp):
    print("This is login by facebook test")


def test_LoginByTwitter(setUp):
    print("This is login by twitter test")


