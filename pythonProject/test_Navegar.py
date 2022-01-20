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
time.sleep(2)

driver.get("https://nextjs.org/docs/basic-features/data-fetching")
time.sleep(2)




# Imprimir el titulo de la página
print(driver.title)

# Finalizar el driver
driver.close()