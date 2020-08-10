from selenium import webdriver
import pytest
import sys
import time


@pytest.mark.windows  # windows is a user specified tag here
def test_windows_1():
    assert True

@pytest.mark.mac   # mac is a user specified tag here
def test_mac_2():
    assert True


@pytest.mark.windows  # windows is a user specified tag here
def test_windows_3():
    assert True