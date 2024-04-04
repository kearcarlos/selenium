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

driver.get("https://www.seleniumeasy.com/test/bootstrap-modal-demo.html")
driver.maximize_window()



#driver.switch_to_alert().accept()  #ejecutar el boton Aceptar
#time.sleep(2)

#driver.switch_to_alert().dismiss()
#driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click()

#driver.find_element_by_xpath("//a[@href='#myModal0']").click()
#time.sleep(2)

#driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[1]")

driver.find_element_by_xpath("//a[@href='#myModal0']").click()
time.sleep(2)
try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]" )))
    Buscar=driver.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click()
    time.sleep(2)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")




time.sleep(4)
driver.close()