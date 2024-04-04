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
nom.send_keys(Keys.TAB + "rodrigo@gmail.com" + Keys.TAB + "Direcccion uno" + Keys.TAB + "Direccion dos "+ Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(2)

driver.find_element_by_xpath("(//span[contains(@class,'text')])[2]").click()

time.sleep(2)
driver.close()