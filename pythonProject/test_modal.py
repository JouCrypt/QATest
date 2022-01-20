# Importar la libreria de webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Cargar el driver


s = Service("C:\Drivers\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# Maximizar el navegador
driver.maximize_window()

t = 1
# Acceder a la url https://demoqa.com/text-box
driver.get("https://sweetalert2.github.io/")

Buscar=driver.find_element(By.XPATH, "//button[@aria-label='Try me! Example: A basic message']")
driver.execute_script("arguments[0].scrollIntoView();", Buscar)
time.sleep(t)
driver.find_element(By.XPATH, "//button[@aria-label='Try me! Example: A basic message']").click()

driver.find_element(By.XPATH, "//button[contains(.,'OK')]").click



time.sleep(t)



# Finalizar el dr

driver.close()