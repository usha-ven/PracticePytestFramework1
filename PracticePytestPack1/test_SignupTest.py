import pytest

@pytest.yield_fixture()
def setUp():
    print("Open URL to Signup")
    yield
    print("Close browser after singup")

def test_signupByEmail(setUp):
    print("This is signup by email test")


def test_signupByFacebook(setUp):
    print("This is signup by facebook test")

def test_signupByTwitter(setUp):
    print("This is signup by twitter test")
