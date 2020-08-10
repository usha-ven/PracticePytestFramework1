import pytest
from selenium import webdriver
import time
from selenium.webdriver.ie.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

ie_options = Options()
ie_options.ignore_protected_mode_settings  = True
path = "C:\Drivers\IEDriverServer_Win32_3.150.1\IEDriverServer"
driver = webdriver.Ie(executable_path=path, options=ie_options)
time.sleep(5)
driver.get("https://www.google.com/")
time.sleep(5)
driver.close()
driver.quit()