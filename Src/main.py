from selenium import webdriver
from time import sleep
from urllib.parse import quote

#https://the-internet.herokuapp.com/basic_auth
user = quote("admin")
password = quote("admin")
url =f'https://{user}:{password}@the-internet.herokuapp.com/basic_auth'
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.get(url)