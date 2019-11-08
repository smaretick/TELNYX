# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#ChromeDriver
driver = webdriver.Chrome()
#browser = webdriver.Firefox()
driver.get("https://telnyx.com/sign-up")
time.sleep(60)
driver.find_element_by_id("email-undefined-objectObject-35667").clear()

time.sleep(60)
driver.find_element_by_id("email-undefined-objectObject-35667").send_keys("scottmaretick51@gmail.com")
driver.find_element_by_id("fullname-undefined-objectObject-32170").clear()
time.sleep(60)
driver.find_element_by_id("fullname-undefined-objectObject-32170").send_keys("scott maretick")
time.sleep(60)
driver.find_element_by_id("password-undefined-objectObject-13080").clear()
time.sleep(60)
driver.find_element_by_id("password-undefined-objectObject-13080").send_keys("Sm110751!")
time.sleep(60)
driver.find_element_by_css_selector("span.CookiePolicyBanner__cookie_button--12Qeu").click()
time.sleep(60)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(60)
driver.find_element_by_id("email-undefined-objectObject-35667").clear()
driver.find_element_by_id("email-undefined-objectObject-35667").send_keys("scott.maretick51@gmail.com")
driver.find_element_by_css_selector("button[type=\"button\"]").click()
driver.find_element_by_id("password-undefined-objectObject-13080").clear()
driver.find_element_by_id("password-undefined-objectObject-13080").send_keys("Jydavis1109!")
driver.find_element_by_id("email-undefined-objectObject-35667").clear()
driver.find_element_by_id("email-undefined-objectObject-35667").send_keys("scott.mitchell.maretick@gmail.com")
driver.find_element_by_id("email-undefined-objectObject-35667").clear()
driver.find_element_by_id("email-undefined-objectObject-35667").send_keys("scott.maretick@gmail.com")
driver.find_element_by_css_selector("button[type=\"button\"]").click()
driver.find_element_by_id("password-undefined-objectObject-13080").clear()
driver.find_element_by_id("password-undefined-objectObject-13080").send_keys("sm1234S!")
driver.find_element_by_xpath("//div[@id='root']/article/div[2]/main/div/div/div/div[2]/div/div/a/div/span[2]/span").click()
driver.find_element_by_css_selector("img").click()
driver.find_element_by_name("internationalPhoneNumber").clear()
driver.find_element_by_name("internationalPhoneNumber").send_keys("+1 708-979-1707")
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.quit()
