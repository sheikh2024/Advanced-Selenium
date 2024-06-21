from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'https://www.selenium.dev/selenium/web/web-form.html'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(3)
def date_picker(date):
  
    date_picker_element = browser.find_element(By.XPATH,"//input[@name='my-date']")
    date_picker_element.send_keys(date)
date_picker("2024-08-23")
time.sleep(3)

input('...')

