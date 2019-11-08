# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Telynx(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://telnyx.com/sign-up"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_telynx(self):
        driver = self.driver
        driver.get(self.base_url + "/sign-up")
        driver.find_element_by_id("email-undefined-objectObject-35667").clear()
        driver.find_element_by_id("email-undefined-objectObject-35667").send_keys("scottmaretick51@gmail.com")
        driver.find_element_by_id("fullname-undefined-objectObject-32170").clear()
        driver.find_element_by_id("fullname-undefined-objectObject-32170").send_keys("scott maretick")
        driver.find_element_by_id("password-undefined-objectObject-13080").clear()
        driver.find_element_by_id("password-undefined-objectObject-13080").send_keys("Sm110751!")
        driver.find_element_by_css_selector("span.CookiePolicyBanner__cookie_button--12Qeu").click()
        driver.find_element_by_xpath("//button[@type='submit']").click()
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
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | authPopup104096 | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=authPopup104096 | ]]
        driver.find_element_by_css_selector("img").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("internationalPhoneNumber").clear()
        driver.find_element_by_name("internationalPhoneNumber").send_keys("+1 708-979-1707")
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
