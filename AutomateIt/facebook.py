#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
print("WebDriver Object", browser)
browser.maximize_window()
browser.get('https://facebook.com')
email = browser.find_element_by_name('email')
password = browser.find_element_by_name('pass')
print("Html elements:")
print("Email:", email, "\nPassword:", password)
#Enter correct email
email.send_keys('abc@gmail.com') 
#Enter correct password
addresspassword.send_keys('pass123') 
browser.find_element_by_id('loginbutton').click()
