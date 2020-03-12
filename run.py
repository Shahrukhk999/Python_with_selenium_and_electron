import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from pageobjects.login import LoginPage
from pageobjects.menu import MainMenu
class unitTest(unittest.TestCase):
    def setUp(self):

        chromedriver_path = r'C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe'
        electron_path = r"C:\Users\user\AppData\Local\Programs\ui.ep.launcher\AAI-EP.exe"

        opts = Options()
        opts.add_argument("--headless")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--start-maximized")
        opts.binary_location = electron_path
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
        self.driver.implicitly_wait(15)  # seconds
 # wait for application to start
    def test_login(self):
        print(self.driver.find_element_by_id("TD-btn_createtest").text)
        self.driver.find_element_by_id("TD-btn_createtest").click()
        time.sleep(5)
        name =self.driver.find_element_by_id("TC-GF-tb_name").get_property("value")
        self.assertEqual("Test 1", name)
        self.driver.find_element_by_id("TC-GF-tb_name").send_keys(Keys.CONTROL, 'a')
        self.driver.find_element_by_id("TC-GF-tb_name").send_keys(Keys.BACK_SPACE)
        self.driver.find_element_by_xpath("//*[@id='TC-GF-radios_testtype']/div/div/div/div[2]/div/div").click()
        self.driver.find_element_by_xpath("//*[@id='TCF-btn_next']/div").click()
        time.sleep(2)
        self.driver.quit()

    @classmethod
    def tearDownClass(self):
        print("testend")
    # self.driver.quit()


if __name__ == '__main__':
    unittest.main()