from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
driver = webdriver.Chrome()

#sleep(10)

# driver.implicitly_wait(10)


wait = WebDriverWait(driver , 10) 

element = wait.until(EC.visibility_of_element_located(By.ID,"element_ip"))



wait = WebDriverWait(driver,10,2,[TimeoutException])

elemnt = wait.until(EC.visibility_of_element_located(by.ID,"my id"))



# code elemnt visile ...