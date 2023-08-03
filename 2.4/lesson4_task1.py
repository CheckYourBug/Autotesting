from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(3)
    browser.find_element(By.CSS_SELECTOR, "#verify").click()
    addin = browser.find_element(By.CSS_SELECTOR, "#verify_message").text
    pyperclip.copy(addin)
    print(addin)
    assert "successful" in addin
finally:
    browser.quit()
