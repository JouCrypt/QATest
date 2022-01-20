# Importar la libreria de webdriver
import time
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class base_test(unittest.TestCase):

    def setUp(self):
        s = Service('C:\Drivers\chromedriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)


    def test1(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        driver = self.driver
        nom=driver.find_element(By.XPATH, "//input[@id='user-name']")
        passw = driver.find_element(By.XPATH, "//input[@id='password']")
        btn = driver.find_element(By.XPATH, "//input[@id='login-button']")

        nom.send_keys("Joseph")
        passw.send_keys(1234567)
        btn.click()

        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error=error.text

        time.sleep(2)

        if(error == 'Epic sadface: Username and password do not match any user in this service'):
            print("Los datos no son correctos")
            print("Prueba uno OK")

    def test2(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        driver = self.driver
        nom=driver.find_element(By.XPATH, "//input[@id='user-name']")
        passw = driver.find_element(By.XPATH, "//input[@id='password']")
        btn = driver.find_element(By.XPATH, "//input[@id='login-button']")

        nom.send_keys("")
        passw.send_keys("loca123")
        btn.click()

        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error=error.text

        time.sleep(2)

        if(error == 'Epic sadface: Username is required'):
            print("Falta el nombre")
            print("Prueba dos OK")

    def test3(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        driver = self.driver
        nom=driver.find_element(By.XPATH, "//input[@id='user-name']")
        passw = driver.find_element(By.XPATH, "//input[@id='password']")
        btn = driver.find_element(By.XPATH, "//input[@id='login-button']")

        nom.send_keys("ksdla")
        passw.send_keys("")
        btn.click()

        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        error=error.text
        print(error)
        time.sleep(2)

        if(error == 'Epic sadface: Password is required'):
            print("Falta el password")
            print("Prueba tres OK")

    def test4(self):
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        driver = self.driver
        nom=driver.find_element(By.XPATH, "//input[@id='user-name']")
        passw = driver.find_element(By.XPATH, "//input[@id='password']")
        btn = driver.find_element(By.XPATH, "//input[@id='login-button']")

        nom.send_keys("standard_user")
        passw.send_keys("secret_sauce")
        btn.click()
        time.sleep(2)
        elemento = driver.find_element(By.XPATH, "//div[@class='app_logo']")
        elemento.is_displayed

        print("EL elemento es: " +str(elemento))
        time.sleep(2)
        '''
        if(error == 'Epic sadface: Password is required'):
            print("Falta el password")
            print("Prueba cuatro OK")
        '''

    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()