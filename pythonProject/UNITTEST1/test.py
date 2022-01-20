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
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/text-box")
        time.sleep(3)

    def test1(self):
        self.driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")

    def tearDown(self):
        self.driver.quit()


    if __name__ == '__main__':
        unittest.main()