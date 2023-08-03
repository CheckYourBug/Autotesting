from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/cats.html")
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, "#button").click()
finally:
    browser.quit()
