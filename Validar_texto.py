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
t=1

driver.get("https://www.seleniumeasy.com/test/input-form-demo.html")
driver.maximize_window()

btn=driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(t)

name_val=driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text
#print("El valor del error es: "+name)
if(name=="Please supply your first name"):
    #print("Falta el nombre")
    cn=driver.find_element_by_xpath("//input[contains(@name,'first_name')]")
    cn.send_keys("Rodrigo")
    time.sleep(2)
    print("Nombre correcto")
else:
    print("Falta el nombre")

time.sleep(t)
ap_val=driver.find_element_by_xpath("//small[@class='help-block'][contains(.,'Please supply your last name')]")
ap=ap_val.text
#print("El valor del error es: "+name)
if(ap=="Please supply your last name"):
    #print("Falta el nombre")
    ap=driver.find_element_by_xpath("//input[contains(@name,'last_name')]")
    ap.send_keys("Villanueva")
    time.sleep(2)
    print("Ap correcto")
else:
    print("Falta el Apellido")

print(btn.is_enabled())
if(btn.is_enabled()==False):
    print("Faltan Campos por Llenar")
else:
    print("Listo todo ok")




time.sleep(t)
driver.close()