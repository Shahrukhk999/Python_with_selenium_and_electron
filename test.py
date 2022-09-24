import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from keyboard import press

class unitTest(unittest.TestCase):
    def setUp(self):
        chromedriver_path = r'chromedriver.exe'
        electron_path = r"Electronapplication exe or app image path"


        opts = Options()
        opts.add_argument("--remote-debugging-port=9222")
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--start-maximized")
        opts.binary_location = electron_path
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
        self.driver.implicitly_wait(15)
 # wait for application to start
    def test_login(self):
        print(self.driver.find_element_by_xpath("").text)

        self.driver.find_element_by_xpath("").click()
        press('enter')
        self.driver.find_element_by_tag_name('').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath("").click()
        self.driver.find_element_by_xpath("").is_displayed()
           @classmethod
    def tearDownClass(self):
        print("testend")
     self.driver.quit()


if __name__ == '__main__':
    unittest.main()
