#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from time import sleep
import unittest
from appium import webdriver
from config import *

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class SelectCam(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(remote_url, desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    # def test_new_cams_page(self):
    #     """
    #     测试页面跳转是否正确
    #     """
    #     drivers = self.driver
    #     sleep(2)
    #     # 点击"+"按钮
    #     image = drivers.find_elements_by_class_name('android.widget.ImageView')
    #     image[0].click()
    #     widget_text = drivers.find_elements_by_class_name("android.widget.TextView")
    #     self.assertEqual(u"添加新的摄像机", widget_text[0].text)
    #     # print widget_text[0].text
    #     drivers.find_elements_by_android_uiautomator("new UiSelector().text('添加新的摄像机')")[1].click()

    def test_turnon_light(self):

        drivers = self.driver
        sleep(1)
        button = drivers.find_elements_by_class_name('android.widget.ImageButton')
        button[2].click()
        sleep(3)
        button2 = drivers.find_element_by_android_uiautomator('new UiSelector().resourceId("io.jjyang.joylite:id/ly_cam_volume_bar")')
        button2.click()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectCam)
    unittest.TextTestRunner(verbosity=2).run(suite)
