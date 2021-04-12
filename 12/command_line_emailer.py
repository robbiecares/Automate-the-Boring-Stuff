#! python3
# command_line_emailer.py - sends an email for you from the command line

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# # take in command line arguments
# recipient = sys.argv[1]
# message = sys.argv[2]

# open your email account in browser

# go to page
browser = webdriver.Firefox()
browser.get('https://mail.google.com/mail/u/0/#inbox')
# htmlElem = browser.find_element_by_tag_name('html')

# enter email addy
user_box = browser.find_element_by_id('identifierId')
user_box.send_keys('robbiecares@gmail.com')

# find next button
buttonElems = browser.find_elements_by_tag_name('button')
for elem in buttonElems:
    if elem.text.lower() == 'weiter':
        next_button = elem

# click next button
next_button.click()
