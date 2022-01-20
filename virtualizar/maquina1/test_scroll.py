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

t = 3
# Acceder a la url https://demoqa.com/text-box
driver.get("https://pixabay.com/es/")

try:
    Buscar = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='app']/div[1]/div[3]/a[1]")))
    Buscar = driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[3]/a[1]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    time.sleep(t)
    driver.find_element(By.XPATH, "//body/div[@id='app']/div[1]/div[3]/a[1]").click()
    time.sleep(t)


except TimeoutException as ex:
    print(ex.msg)
    print("Elemento no disponible")

#tiempo de salida
time.sleep(t)



# Finalizar el driver
driver.close()