#Importar la libreria de webdriver

import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from Funciones.Funciones import Funciones_Globales


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
        f=Funciones_Globales(driver)
        f.navegar("https://demoqa.com/text-box", 2)

    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
        unittest.main()