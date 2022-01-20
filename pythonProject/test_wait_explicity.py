# Importar la libreria de webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Cargar el driver


s = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Maximizar el navegador
driver.maximize_window()

driver.implicitly_wait(10)




t = 2
# Acceder a la url
driver.get("https://demoqa.com/automation-practice-form")

#scroll a la página para quitar el banner
driver.execute_script("window.scrollTo(0,350)")
time.sleep(t)

diaSelect = driver.find_element(By.XPATH, "//div[contains(text(),'Select State')]").click()
ds = Select(diaSelect)

ds.select_by_index(1)

#tiempo de salida
time.sleep(t)




# Finalizar el driver
driver.close()