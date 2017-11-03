#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
from time import sleep
import unittest
from appium import webdriver
from config import *
from HTMLTestRunner import HTMLTestRunner

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class SelectCam(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(remote_url, desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_live(self):
        drivers = self.driver
        online = drivers.find_elements_by_xpath('.//android.widget.ListView/../android.widget.TextView')
        sleep(2)
        print online
        # self.assertEqual(online, u'在线')
        live = drivers.find_elements_by_id('io.jjyang.joylite:id/img_live_video')
        live[0].click()
        back = drivers.find_elements_by_id('io.jjyang.joylite:id/img_title_back')
        back[0].click()

    def test_turn_on_light(self):

        drivers = self.driver
        sleep(1)
        button = drivers.find_elements_by_class_name('android.widget.ImageButton')
        button[2].click()
        sleep(3)
        button2 = drivers.find_element_by_id('io.jjyang.joylite:id/toggle_btn_cam_cue_light')
        button2.click()
        sleep(2)

    def test_swip(self):
        drivers = self.driver
        sleep(5)
        name = drivers.find_elements_by_id("io.jjyang.joylite:id/txt_cam_name")
        if name[0] != 's201':
            drivers.swipe(992, 1565, 135, 219, 1000)
        else:
            name[0].click()

        sleep(5)



if __name__ == '__main__':

    fp = open('./report/results_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u'Joylite功能测试报告',
        description=u"测试用例执行情况：")
    suite = unittest.TestLoader().loadTestsFromTestCase(SelectCam)
    runner.run(suite)