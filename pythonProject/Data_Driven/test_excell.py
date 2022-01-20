
import unittest

from Func_EX import *

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service

from Funciones.Funciones import Funciones_Globales
from Func_EX import Funexcel
tg = .5
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
        fe = Funexcel(driver)
        f.navegar("https://demoqa.com/text-box", 2)
        ruta = "C://Users//G-UNIT//Documents//Prueba selenium//Libro1.xlsx"
#contar las rutas
        filas = fe.getRowCount(ruta, "Sheet")
        print(filas)
#r=recorrer el excel empieza a leer en el 2
        for r in range(2,filas+1):
            nombre = fe.readData(ruta,"Sheet",r,1)
            email = fe.readData(ruta,"Sheet", r, 2)
            dir1 = fe.readData(ruta,"Sheet", r, 3)
            dir2 = fe.readData(ruta,"Sheet", r, 4)

            f.Texto_Mixto("id","userName",nombre,tg)
            f.Texto_Mixto("id","userEmail",email, tg)
            f.Texto_Mixto("id","currentAddress",dir1, tg)
            f.Texto_Mixto("id","permanentAddress",dir2, tg)
            f.Click_Mixto("id","submit",tg)

            e=f.Existe("id","name",tg)
            if(e=="Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta,"Sheet",r,5,"Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta,"Sheet",r,5,"Error")


    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


