import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
num_1 = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap").text
num_2 = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap").text
s = str(int(num_1) + int(num_2))
lis_t = browser.find_element(By.CSS_SELECTOR, "select#dropdown.custom-select")
lis_t.click()
val_s = browser.find_element(By.CSS_SELECTOR, "[value='" + s + "']")
val_s.click()
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
