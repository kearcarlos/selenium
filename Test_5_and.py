import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(1)

nom=driver.find_element_by_xpath("//input[@type='text' and @id='userName']")
nom.send_keys("Rodrigo")
time.sleep(1)
driver.find_element_by_id("userEmail").send_keys("rodrigo@gmail.com")
time.sleep(1)
driver.find_element_by_id("currentAddress").send_keys("Dirección uno")
time.sleep(1)
driver.find_element_by_id("permanentAddress").send_keys("Dirección dos")
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element(By.ID,"submit").click()
time.sleep(2)

driver.close()