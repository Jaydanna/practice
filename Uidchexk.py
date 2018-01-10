# -*- coding:utf-8 -*-  
# author:Jaydan
import selenium
import Readexcel
from selenium import webdriver
import unittest
from Readexcel import read_excel
from time import sleep

file = r'F:\GitHub\practice\DATA\Test.xlsx'

class CheckUid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://uid.iotcplatform.com:10000/index.php"

    def tearDown(self):
        self.driver.quit()

    def test_UID(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_name("uid").clear()
        for i in
        data = read_excel(file,0,0,0)[0]
        driver.find_element_by_name("uid").send_keys(data)
        sleep(4)
        driver.find_element_by_name('connect').click()

if __name__ == "__main__":
    unittest.main()