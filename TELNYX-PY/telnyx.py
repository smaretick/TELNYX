# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
###############################################################################################
#desired_cap = {
#    'browserName': 'iPhone',
#        'device': 'iPhone 7',
#            'realMobile': 'true',
#                'os_version': '10.3'
#}

#browser = webdriver.Remote(
#                          command_executor='http://smaretick3:gqzxib7a1Gwg8bbNAyNm@hub.browserstack.com:80/wd/hub',
#                          desired_capabilities=desired_cap)
###############################################################################################
#
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = '/Volumes/Untitled/Applications/Firefox.app/Contents/MacOS/firefox'
browser = webdriver.Firefox(capabilities=firefox_capabilities)
browser.get("https://telnyx.com/")
print (browser.title)
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").send_keys("scottmaretick51@gmail.com")

#browser.find_element_by_xpath(".//*[@id='root']/article/div[2]/main/div/div/div/div[2]/form/div[5]/div/button").click() #CREATE MY ACCOUNT
time.sleep(10);
browser.quit()
