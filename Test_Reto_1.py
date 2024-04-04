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

driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
driver.maximize_window()
time.sleep(t)

driver.find_element_by_xpath("//input[contains(@name,'first_name')]").send_keys("Juan"+ Keys.TAB + "Perez" + Keys.TAB + "juan@gmail.com")
driver.find_element_by_xpath("//input[contains(@name,'phone')]").send_keys("3453456754"+ Keys.TAB+"Calle 643 #23"+ Keys.TAB+"CDMX")
estado=Select(driver.find_element_by_xpath("//select[contains(@name,'state')]"))
estado.select_by_index(5)
driver.find_element_by_xpath("//input[contains(@name,'zip')]").send_keys("07867"+ Keys.TAB+"demouno.com.mx")
driver.find_element_by_xpath("//input[contains(@value,'yes')]").click()

driver.find_element_by_xpath("//textarea[contains(@class,'form-control')]").send_keys("Proyecto Reto Uno"+Keys.TAB+Keys.ENTER)





time.sleep(t)
driver.close()



'''
try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")))
    Buscar=driver.find_element_by_xpath("//a[@href='/es/images/search/?order=ec'][contains(.,'Descubre más')]")
    ir=driver.execute_script("arguments[0].scrollIntoView();",Buscar)
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
'''