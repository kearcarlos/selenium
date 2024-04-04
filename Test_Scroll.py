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
t=3

driver.get("https://pixabay.com/es/")
driver.maximize_window()
time.sleep(t)

#driver.execute_script("window.scrollTo(0,1500)")


try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")))
    Buscar=driver.find_element_by_xpath("//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")





time.sleep(t)
driver.close()