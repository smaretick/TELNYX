# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#PYTHON (/usr/bin/python)
#SELENIUM (pip install selenium)
#brew cask install chromedriver
#brew cask reinstall chromedriver
#which chromedriver
#/usr/local/bin/chromedriver
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
################################################################################################################################
#SIP Trunking, Voice and Messaging Solutions
#TELYNX https://telnyx.com/
driver.get("https://telnyx.com/")  #TELYNX
driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").clear()  #email
#driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").send_keys("smaretick@hotmail.com") #hotmail
#driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").send_keys("scott.mitchell.maretick@gmail.com") #gmail
driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").send_keys("scottABC@gmail.com") #non existent gmail
driver.find_element_by_css_selector(".SubmitButton__submitButton--3tXYG.CtaButton__ctaButton--1FUS2.CtaButton__button--aL6zF.CtaButton__coral--tAvYx").click()  #Try Telnyx
#CREATE FREE ACCOUNT=============================================================================================================
#APPENDS EMAIL ON TO EXISTING EMAIL EVEN THOUGH FIELD IS CLEARED WITH SELENIUM
#xpath = .//*[@id='email-undefined-objectObject-12313']  (dynamic element can't use)
#xpath = .//input[starts-with(@id, 'email')]   (element works)
driver.find_element_by_xpath(".//input[starts-with(@id, 'email')]").clear()  #email
driver.find_element_by_xpath(".//input[starts-with(@id, 'email')]").send_keys("scottabc@gmail.com") #non existent gmail
#================================================================================================================================
#WORKS THRU HERE
driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").send_keys("scotty@gmail.com") #non existent gmail
driver.find_element_by_xpath(".//input[starts-with(@id, 'fullname')]").send_keys("Scott Maretick")  #FULL NAME
driver.find_element_by_xpath(".//input[starts-with(@id, 'password')]").send_keys("Sm110751!")  #PASSWORD
driver.find_element_by_css_selector(".SubmitButton__submitButton--3tXYG.CtaButton__ctaButton--1FUS2.CtaButton__button--aL6zF.CtaButton__coral--tAvYx").click() #CREATE MY ACCOUNT
#VERIFY YOUR ACCOUNT
driver.find_element_by_css_selector(".FormPhoneNumberField__textField--I-stL.FormMaskedField__formMaskedField--_nTnH").clear()  #PHONE NUMBER
driver.find_element_by_css_selector(".FormPhoneNumberField__textField--I-stL.FormMaskedField__formMaskedField--_nTnH").send_keys("17089791707")  #PHONE NUMBER
driver.find_element_by_css_selector(".SubmitButton__submitButton--3tXYG.CtaButton__ctaButton--1FUS2.CtaButton__button--aL6zF.CtaButton__coral--tAvYx").click() #SEND MY CODE
#driver.find_element_by_css_selector(".FormPhoneNumberField__textField--I-stL.FormMaskedField__formMaskedField--_nTnH").send_keys("7152")  #VERIFY MY ACCOUNT
driver.find_element_by_xpath(".//*[@id='confirmationCode']/article/div[2]/main/div/div/div/div[2]/form/div[5]/div/button").click()

#has already been taken, Another account already exists that resolves to the same Gmail account
#CREATE a FREE ACCOUNT PAGE  https://telnyx.com/sign-up?email=smaretick%40hotmail.com
driver.find_element_by_xpath(".//input[starts-with(@id, 'email')]").clear  #email  DOESN'T CLEAR FIELD
driver.find_element_by_xpath(".//input[starts-with(@id, 'email')]").send_keys("smaretick@gmail.com")  #email
#driver.find_element_by_xpath(".//*[@id='root']/article/div[2]/main/div/div/div/div[2]/form/div[6]/div/button").click()
driver.find_element_by_css_selector(".SubmitButton__submitButton--3tXYG.CtaButton__ctaButton--1FUS2.CtaButton__button--aL6zF.CtaButton__coral--tAvYx").click()

#CREATE MY ACCOUNT WITH GOOGLE
driver.find_element_by_xpath(".//*[@id='root']/article/div[2]/main/div/div/div/div[2]/div/div/a/div/span[2]/span").click()  #open popup
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            google_window_handle = handle
            break
driver.switch_to.window(google_window_handle)
#email or phone

#NEXT

# Create account (First name, Last name, Password, Confirm password, NEXT BUTTON, Sign in instead)

#driver.current_window_handle #main page window handle
#driver.switch_to.window(window_handle)
#driver.switch_to_default_content() #returns to main page
#driver.quit() #closes browser
#time.sleep(60)
                                    
                                    
                                    
                                    
                                    
                                    
