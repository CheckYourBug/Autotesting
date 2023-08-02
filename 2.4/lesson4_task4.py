from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(var):
  return str(math.log(abs(12*math.sin(int(var)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    #проверяем элемент каждые 0,5с в течение 5 секунд, пока элемент не станет активным and click
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.CSS_SELECTOR, "#book").click()
    var = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    xvar = calc(var)
    print(xvar)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(xvar)
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()
    time.sleep(5)
    alert2 = browser.switch_to.alert.text
    addin = alert2.split(': ')[-1]
    pyperclip.copy(addin)
    print(addin)

finally:
    browser.quit()
