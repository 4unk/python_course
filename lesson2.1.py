from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(get_secret):
    return str(math.log(abs(12*math.sin(int(get_secret)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    secret = browser.find_element(By.CSS_SELECTOR, "#treasure")
    get_secret = secret.get_attribute("valuex")
#    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    #x = .n
    y = calc(get_secret)
    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)
    opt = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    opt.click()
    opt1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    opt1.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
