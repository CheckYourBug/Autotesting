import time

from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_lang(browser):
    browser.get(link)
    time.sleep(10)
    assert browser.find_elements(By.CSS_SELECTOR, "input+[type='submit']"), 'basket button not found'