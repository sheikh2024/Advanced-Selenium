from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.selenium.dev/selenium/web/web-form.html'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

input_text = browser.find_element(By.ID, 'my-text-id')
input_text.send_keys('hamzeh')

input_password = browser.find_element(By.XPATH, "//input[@name='my-password']")
input_password.send_keys('password')

input('...')