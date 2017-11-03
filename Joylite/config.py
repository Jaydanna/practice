#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: samren


chrome_driver = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
remote_url = 'http://localhost:4723/wd/hub'
desired_caps = {'platformName': 'Android',
                'platformVersion': 6.0,
                'deviceName': '5LM7N16415016718',
                'appPackage': 'io.jjyang.joylite',
                'appActivity': '.SplashActivity',
                'noReset': 'true'}
