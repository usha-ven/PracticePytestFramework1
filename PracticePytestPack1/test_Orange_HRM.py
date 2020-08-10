from selenium import webdriver
import pytest
import time

class TestOrangeHRM():

    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.26.0-win32\geckodriver.exe")
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_homePageTitle(self, test_setup):
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        assert self.driver.title=="OrangeHRM"

    def test_pyloginTest(self,test_setup):
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()

