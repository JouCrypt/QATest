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
driver.get("https://abstracta.us/blog/software-testing/best-demo-websites-for-practicing-different-types-of-software-tests/")

#obteniendo los enlaces de la pagina
links = driver.find_elements(By.TAG_NAME, "a")

print("El numero que hay en la página es:", len(links))

#tiempo de salida
'''for num in links:
    print(num.text)
'''
buscar=driver.find_element(By.LINK_TEXT, "Solutions")
driver.find_element(By.LINK_TEXT, "Test Automation").click()
time.sleep(t)



# Finalizar el dr

driver.close()