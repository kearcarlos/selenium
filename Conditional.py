import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
t=2

driver.get("https://demoqa.com/")
driver.maximize_window()

titulo=driver.find_element_by_xpath("//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1=driver.find_element_by_xpath("(//div[contains(@class,'card-up')])[1]")

if(titulo.is_displayed()==True):
    print("Existe la imagen")
    btn1.click()
    time.sleep(2)
else:
    print("No existe la imagen")


time.sleep(2)
driver.close()