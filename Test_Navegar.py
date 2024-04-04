import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

t=3
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(t)

driver.get("https://www.selenium.dev/es/documentation/webdriver/locating_elements/")
time.sleep(t)

driver.get("https://www.codegrepper.com/code-examples/python/selenium+send+enter+key")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

driver.execute_script("window.history.go(-1)")
time.sleep(t)

#driver.forward()
driver.execute_script("window.history.go(2)")
time.sleep(t)



driver.close()



