from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait2.html")
    #проверяем элемент каждые 0,5с в течение 5 секунд, пока элемент не станет активным and click
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    ).click()
    addin = browser.find_element(By.CSS_SELECTOR, "#verify_message").text
    pyperclip.copy(addin)
    print(addin)
    assert "successful" in addin
finally:
    browser.quit()
