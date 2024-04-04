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
t=.5

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
time.sleep(t)

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element_by_xpath("//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://Users//Usuario1//PycharmProjects//Curso_selenium//Imagenes//demo1.jpg")
    time.sleep(t)
    driver.find_element_by_xpath("//input[contains(@id,'itsanimage')]").click()
    driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
    time.sleep(t)



except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")





time.sleep(t)
driver.close()