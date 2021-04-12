#! python3
# 2048.py - plays the game 2048 as hosted on https://play2048.co/

from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

# open page & allow to load
browser = webdriver.Firefox()
browser.get('https://play2048.co/')
time.sleep(5)

# accept cookies
try:
    cookies_button = browser.find_element_by_link_text('Verstanden!')
    cookies_button.click()
except NoSuchElementException:
    pass

# capture html doc (to interact with page)
htmlElem = browser.find_element_by_tag_name('html')


def check_game_state():
    """determine if the current game is still active"""
    try:
        browser.find_element_by_link_text('Try again')
    except NoSuchElementException:
        return True
    return False


# check for game over condition
game_active = check_game_state()

# play game
while game_active:
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)

    # check for game over condition
    game_active = check_game_state()
