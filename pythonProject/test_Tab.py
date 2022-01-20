# Importar la libreria de webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Cargar el driver


s = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Maximizar el navegador
driver.maximize_window()

# Acceder a la url https://demoqa.com/text-box
driver.get("https://demoqa.com/text-box")

#tiempo de salida
time.sleep(1)

#buscar el elemento xpath
nomb = driver.find_element(By.XPATH, "//input[@id='userName']")
nomb.send_keys("Joseph")
nomb.send_keys(Keys.TAB + "123josep@gmail.com" + Keys.TAB + "Panamá" + Keys.TAB + "Chiriqui" + Keys.TAB + Keys.ENTER)
time.sleep(2)


#scroll a la página
driver.execute_script("window.scrollTo(0,350)")
time.sleep(2)
driver.find_element(By.XPATH, "//li[contains(.,'Check Box')]").click()
time.sleep(2)





# Imprimir el titulo de la página
print(driver.title)

# Finalizar el driver
driver.close()