# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
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
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=email-undefined-objectObject-26831 | ]]
        driver.find_element_by_id("email-undefined-objectObject-26831").click()
        driver.find_element_by_id("email-undefined-objectObject-26831").clear()
        driver.find_element_by_id("email-undefined-objectObject-26831").send_keys("scott.mitchell.maretick@gmail.com")
        driver.find_element_by_xpath("//button[@type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
