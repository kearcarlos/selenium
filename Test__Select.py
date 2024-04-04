import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
t=2

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()
time.sleep(2)

select1=driver.find_element_by_xpath("//select[contains(@id,'select-demo')]")
dias=Select(select1)

dias.select_by_visible_text("Sunday")
time.sleep(t)

dias.select_by_index(2)
time.sleep(t)

dias.select_by_value("Thursday")
time.sleep(t)

#segundo bloque

ciudad=Select(driver.find_element_by_id("multi-select"))

ciudad.select_by_value("California")
time.sleep(t)
ciudad.select_by_value("New York")
time.sleep(t)
ciudad.select_by_index(2)
time.sleep(t)


driver.close()