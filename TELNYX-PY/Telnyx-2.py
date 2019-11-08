# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#FIREFOX
#firefox_capabilities = DesiredCapabilities.FIREFOX
#firefox_capabilities['marionette'] = True
#firefox_capabilities['binary'] = '/Volumes/Untitled/Applications/Firefox.app/Contents/MacOS/firefox'
#driver = webdriver.Firefox(capabilities=firefox_capabilities)
#CHROME
driver = webdriver.Chrome("/Users/scottmaretick/Desktop/chromedriver")
driver.get("https://telnyx.com/")
driver.find_element_by_name("email").click()
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("scottmaretick51@gmail.com")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.find_element_by_id("fullname-undefined-objectObject-56542").click()
driver.find_element_by_id("fullname-undefined-objectObject-56542").clear()
driver.find_element_by_id("fullname-undefined-objectObject-56542").send_keys("SCOTT MARETICK")
driver.find_element_by_id("password-undefined-objectObject-5492").clear()
driver.find_element_by_id("password-undefined-objectObject-5492").send_keys("Sm110751!")
driver.find_element_by_xpath("//div[@id='root']/article/div[2]/main/div/div/div/div[2]/form/div[5]/div/button/span").click()
driver.find_element_by_id("email-undefined-objectObject-26831").click()
driver.find_element_by_id("email-undefined-objectObject-26831").click()
driver.find_element_by_id("email-undefined-objectObject-26831").click()
driver.find_element_by_id("email-undefined-objectObject-26831").clear()
driver.find_element_by_id("email-undefined-objectObject-26831").send_keys("scott.mitchell.maretick@gmail.com")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.quit()
