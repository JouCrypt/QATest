# Importar la libreria de webdriver
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains
from Funciones.Funciones import Funciones_Globales



#Cargar el driver

tg = 1

class base_test(unittest.TestCase):

    def setUp(self):
        s = Service('C:\Drivers\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)
        '''self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(3)'''

    def test(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://opensource-demo.orangehrmlive.com/", tg)
        f.Texto_Mixto("xpath", "//input[contains(@id,'txtUsername')]", "Admin", tg)
        f.Texto_Mixto("xpath", "//input[contains(@id,'txtPassword')]", "admin123", tg)
        f.Click_Mixto("xpath", "//input[contains(@id,'btnLogin')]", tg)

        admin = driver.find_element(By.ID, "menu_admin_viewAdminModule")
        sub1 = driver.find_element(By.ID, "menu_admin_UserManagement")
        sub2 = driver.find_element(By.ID, "menu_admin_viewSystemUsers")

        act = ActionChains(driver)
        act.move_to_element(admin).move_to_element(sub1).move_to_element(sub2).click().perform()




    def tearDown(self):
            self.driver.quit()

    if __name__ == '__main__':
        unittest.main()