from selenium import webdriver
from selenium.webdriver.common.by import By


url='https://seleniumpractise.blogspot.com/2016/09/how-to-work-with-disable-textbox-or.html'
script="document.getElementById('pass').removeAttribute('disabled')"
options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=options)
driver.get(url)
driver.execute_script(script)
driver.find_element(By.ID, 'pass').send_keys('password')