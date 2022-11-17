import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value").text
x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
x = calc(x_element)
ans = browser.find_element(By.CSS_SELECTOR, "#answer")
ans.send_keys(x)
robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robot_checkbox.click()
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
robot_rule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robot_rule.click()
button.click()
time.sleep(5)
browser.quit()


