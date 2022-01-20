# Importar la libreria de webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Cargar el driver
from selenium.webdriver.chrome.service import Service

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
time.sleep(1)

driver.find_element(By.XPATH, "//input[@id='userEmail']").send_keys("123josep@gmail.com")
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Panamá")
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Provincia")
time.sleep(1)

#scroll a la página para quitar el banner
driver.execute_script("window.scrollTo(0,350)")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@id='submit']").click()
time.sleep(2)

# Imprimir el titulo de la página
print(driver.title)

# Finalizar el driver
driver.close()