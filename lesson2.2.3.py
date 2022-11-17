from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
field1 = browser.find_element(By.NAME, "firstname")
field1.send_keys("Alex")
field2 = browser.find_element(By.NAME, "lastname")
field2.send_keys("Green")
field3 = browser.find_element(By.NAME, "email")
field3.send_keys("alex.green@gmail.com")
cd = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(cd, 'test.txt')
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
time.sleep(5)
browser.quit()