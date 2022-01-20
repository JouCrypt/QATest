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
t = 1
# Acceder a la url https://demoqa.com/text-box
driver.get("https://demoqa.com")

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")

print(titulo.is_displayed())

bt1 = driver.find_element(By.XPATH, "(//div[@class='card-up'])[1]")
if(titulo.is_displayed()==True):
    print("Existe la imagen")
    bt1.click()
else:
    print("No existe la imagen")
#tiempo de salida
time.sleep(t)


# Finalizar el driver
driver.close()