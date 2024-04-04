import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
driver.implicitly_wait(15)

t=.1
time.sleep(t)

nom=driver.find_element_by_css_selector("#userName")
nom.send_keys("Rodrigo")
time.sleep(t)
driver.find_element_by_css_selector("#userEmail").send_keys("rodrigo@gmail.com")
time.sleep(t)
driver.find_element_by_xpath("//textarea[contains(@id,'currentAddress')]").send_keys("Dirección uno")
time.sleep(t)
driver.find_element_by_xpath("//textarea[contains(@id,'permanentAddress')]").send_keys("Dirección dos")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(t)

driver.find_element_by_xpath("//button[contains(@id,'submit')]").click()
time.sleep(t)

driver.close()