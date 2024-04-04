import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
driver.maximize_window()
#driver.implicitly_wait(10)
t=.5

btn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#'][contains(.,'No, thanks!')]")))
btn.click()


driver.find_element_by_xpath("//input[contains(@id,'user-message')]").send_keys("Bienvenidos a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)

driver.find_element_by_xpath("//input[contains(@id,'sum1')]").send_keys("5"+ Keys.TAB+ "5"+ Keys.TAB + Keys.ENTER)




time.sleep(t)
driver.close()