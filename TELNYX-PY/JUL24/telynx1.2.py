# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
################################################################################################################################
#SIP Trunking, Voice and Messaging Solutions
driver = webdriver.Firefox()
#driver = webdriver.Chrome()
driver.get("https://telnyx.com/")  #TELYNX
driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").clear()  #email
driver.find_element_by_css_selector(".EmailFormCta__inputWrapper--2so5Q>input").send_keys("scottmaretick51@gmail.com") #gmail
driver.find_element_by_css_selector(".SubmitButton__submitButton--3tXYG.CtaButton__ctaButton--1FUS2.CtaButton__button--aL6zF.CtaButton__coral--tAvYx").click()  #Try Telnyx
time.sleep(10)
window_before_handle = driver.window_handles[0]
print ("window_before_handle is:") #window_before
print window_before_handle
driver.find_element_by_xpath(".//*[@id='root']/article/div[2]/main/div/div/div/div[2]/div/div/a/div/span[2]/span").click()  #BRINGS UP POP UP
#WORKS THRU HERE BUT NEED TO FIND EMAIL ADDRESS TO CONTINUE


#XPATH = //*[@id="identifierId"]
#CSS PATH html.CMgTXc body#yDmH0d.nyoS7c.SoDlKd.EIlDfe div.H2SoFe.LZgQXe.TFhTPc div#initialView.RAYh1e.LZgQXe.qmmlRd div.xkfVF div#view_container.JhUD8d.SQNfcc div div.DRS7Fe.bxPAYd.k6Zj8d div.pwWryf.bxPAYd div.Wxwduf.Us7fWe.JhUD8d div.WEQkZc div form content div.cDSmF div.rFrNMe.KSczvd.uyaebd.vHVGub.zKHdkd.sdJrJc.Tyc9J div.aCsJod.oJeWuf div.aXBtI.Wic03c div.Xb9hP input#identifierId.whsOnd.zHQkBf
#CSS = #identifierId
#CREATE MY ACCOUNT WITH GOOGLE===================================================================================================
window_after_handle = driver.window_handles[1]
print ("window_after_handle is:") #window_after
print window_after_handle
driver.switch_to_window(window_after_handle)
current_window_handle = driver.current_window_handle
print ("current_window_handle is:") #current_window_handle
print current_window_handle
#//*[@id="identifierId"]
#driver.find_element_by_css_selector("#identifierId").send_keys("scottmaretick51@gmail.com") #gmail
#driver.find_element_by_css_selector("#email").send_keys("scottmaretick51@gmail.com") #gmail
##driver.find_element_by_xpath(".//input[starts-with(@id, 'identifierId')]").send_keys("scottmaretick51@gmail.com")  #email
##driver.find_element_by_xpath(".//input[contains(@id, 'identifierId')]").send_keys("scottmaretick51@gmail.com")  #email
#driver.findElement(By.xpath("//* [start-with(@id,'identifierId')]"))


time.sleep(10)
#driver.find_element_by_xpath("//*[@id=identifierId]").send_keys("scottmaretick51@gmail.com")  #email
#popup email xpath == //*[@id="identifierId"]
#POPUP==Sign in with Google
#driver.switch_to_window("Sign in with Google")
#signin_window_handle = None
#while not signin_window_handle:
#    for handle in driver.window_handles:
#        if handle != main_window_handle:
#            google_window_handle = handle
#            print main_window_handle
#            print google_window_handle
#            break
#driver.switch_to.window(google_window_handle)
#driver.quit() #closes browser

                                    
                                    
                                    
                                    
                                    
