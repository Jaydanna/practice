# -*- coding:utf-8 -*-  
# author:Jaydan
import selenium
import Readexcel
from selenium import webdriver
import unittest
from Readexcel import read_excel
from time import sleep

file = r'..\\practice\DATA\UID.xlsx'

class CheckUid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://uid.iotcplatform.com:10000/index.php"

    def tearDown(self):
        self.driver.quit()

    # def test_UID(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.find_element_by_name("uid").clear()
    #     num = read_excel(file, 3)
    #     for i in range(len(num)):
    #         uidselector = driver.find_element_by_name("uid")
    #         if uidselector == '':
    #             data = num[1]
    #             uidselector.send_keys(data)
    #             driver.find_element_by_name('connect').click()
    #             sleep(5)
    #             a = driver.find_element_by_xpath("/html/body/p[2]/text()[3]")
    #             print i,a
    def testfoeme(self):
        driver = self.driver
        driver.get(self.base_url)
        num = read_excel(file, 3)
        uidselector = driver.find_element_by_name("uid")
        data = num[1]
        uidselector.send_keys('MYMPBHTB2X96DPBR111A')
        driver.find_element_by_name('connect').click()
        sleep(5)
        # a = driver.find_elements_by_css_selector("css= br + br")
        a = driver.find_elements_by_xpath("/html/body").get_attribute('p')
        print a

        if 'IOTC_Connect(): FAIL(-90)' in a:
            print 'right!'
        elif '11SGERZ8DJZTFP7W111A' in a:
            raise RuntimeError('is active!')
        else:
            raise NameError('input file name error !')



if __name__ == "__main__":
    unittest.main()