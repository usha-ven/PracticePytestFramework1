from selenium import webdriver
import pytest
import sys
import time

@pytest.mark.skip
def test_demo_1():
    assert True

@pytest.mark.skip(reason = "Not required to test")
def test_demo_2():
    assert True


def test_demo_3():
    assert True


@pytest.mark.skipif(sys.version_info > (3,6), reason= "requires python 3.6 or highter")
def test_demo_4():
    assert True

@pytest.mark.windows
def test_demo_5():
    assert True

@pytest.mark.mac
def test_demo_5():
    assert True


