# Importar la libreria de webdriver
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class Funciones_Globales():

    def __init__(self,driver):
        self.driver = driver

    def navegar(self, url, Tiempo):
        self.driver.implicitly_wait(30)
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t
    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url, Tiempo):
        self.driver.get(Url)
        self.driver.maximize_window()
        print("Página abierta: " + str(Url))
        t = time.sleep(Tiempo)
        return t

    def SELXPATH(self,tipo,selector):
        if(tipo == "xpath"):
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, selector)
        elif(tipo == "id"):
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, selector)
        return val


    def Texto_Mixto(self, tipo, selector, texto, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SELXPATH(tipo,selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SELXPATH(tipo, selector)
                val.clear()
                val.send_keys(texto)
                print("Escribiendo en el campo {} el texto -> {} ".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Click_Mixto(self, tipo, selector, tiempo):
            if (tipo == "xpath"):
                try:
                    val = self.SELXPATH(tipo,selector)
                    val.click()
                    print("dando click en {} -> {} ".format(selector, selector))
                    t = time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Elemento" + selector)
                    return t
            elif (tipo == "id"):
                try:
                    val = self.SELXPATH(tipo,selector)
                    val.click()
                    print("dando click en {} -> {} ".format(selector, selector))
                    t = time.sleep(tiempo)
                    return t
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Elemento" + selector)
                    return t

    def Existe(self,tipo,selector,tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SELXPATH(tipo,selector)
                val.click()
                print("El elemento {} -> existe ".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return "No Existe"
        elif (tipo == "id"):
                try:
                    val = self.SELXPATH(tipo,selector)
                    val.click()
                    print("El elemento {} -> existe ".format(selector))
                    t = time.sleep(tiempo)
                    return "Existe"
                except TimeoutException as ex:
                    print(ex.msg)
                    print("No se encontro el Elemento" + selector)
                    return "No Existe"

    def Click_Mouse(self, tipo, selector, tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SELXPATH(tipo,selector)


                act = ActionChains(self.driver)

                if (selector == "doubleClickBtn"):
                    act.double_click(val).click().perform()
                    print("Dando doble-click en el elemento {}".format(selector))
                if (selector == 'rightClickBtn'):
                    act.context_click(val).click().perform()
                    print("Dando click-derecho en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SELXPATH(tipo,selector)
                act = ActionChains(self.driver)


                if (selector == "doubleClickBtn"):
                    act.double_click(val).click().perform()
                    print("Dando doble-click en el elemento {}".format(selector))
                if (selector == 'rightClickBtn'):
                    act.context_click(val).click().perform()
                    print("Dando click-derecho en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Drag_Drop(self, tipo,selector,destino,tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SELXPATH(tipo, selector)
                val2 = self.SELXPATH(tipo, destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val,val2).perform()
                print("Moviendo el elemento {} => {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t
        elif (tipo == "id"):
            try:
                val = self.SELXPATH(tipo, selector)
                val2 = self.SELXPATH(tipo, destino)
                act = ActionChains(self.driver)
                act.drag_and_drop(val, val2).perform()
                print("Moviendo el elemento {} => {}".format(selector, destino))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el Elemento" + selector)
                return t

    def Salida(self):
            print("Se termina la prueba Exitosamente")
