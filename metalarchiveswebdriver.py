#!  /usr/bin/env python
# This is the webdriver method for searching for a band and getting data back.
#  This may help.
from selenium import webdriver



browser = webdriver.Firefox()
browser.get('http://www.metal-archives.com/')
print('Welcome to the interactive metal archives web driver thingy.')
print('What band would you like to look up now?')
bandname = input('Please enter a band name here:   ')
text_area = browser.find_element_by_id('searchQueryBox')
text_area.send_keys(bandname)
python_button = browser.find_element_by_xpath('html/body/div/div/div/form/div/button')
python_button.click()
