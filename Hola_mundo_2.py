from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")


driver.get("https://demoqa.com/text-box")
print("Bienvenido a Selenium")
print(driver.title)

driver.close()
