# Importar la libreria de webdriver
import time
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


from Funciones.Funciones import Funciones_Globales

#Cargar el driver

tg = 1.5

class base_test(unittest.TestCase):

    def setUp(self):
        s = Service('C:\Drivers\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def test(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.navegar("https://demo.guru99.com/test/drag_drop.html#google_vignette", tg)

        f.Drag_Drop("id", "credit1", "loan", tg)
        f.Drag_Drop("id", "credit2", "bank", tg)
        f.Drag_Drop("id", "fourth", "amt7", tg)
        f.Drag_Drop("id", "fourth", "amt8", tg)


    time.sleep(tg)

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()