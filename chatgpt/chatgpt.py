# moldulos de python
import os
import sys
import time
import pickle
import tempfile

# modulos de terceros
from selenium.webdriver.common.by import By  # para buscar por tipos de elemento
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys  # para pulsar teclas especiales
from selenium.webdriver.support.ui import WebDriverWait  # para esperar en selenium
from selenium.common.exceptions import TimeoutException

# propios
from apps.oculto import Iniciar_driver
from funcion import esperar_boton_detener_generacion

user = "camilo"
password = "alca"


class Programa:
    def __init__(self, user, password):
        """
        Iniciamos webdriver y nos logueamos en ChatGpt
        """
        self.OPENAI_USER = user
        self.OPENAI_PASS = password
        self.COOKIES_FILE = f"{tempfile.gettempdir()}/openai.cookies"
        self.driver = Iniciar_driver(pos="izquierda")
        self.wait = WebDriverWait(self.driver, 30)
        login = self.login_openai()
        print()

    def login_openai(self):
        """
        Realizara login en open ai por cookies o desde cero (guarda las cookies)
        """
        print("login desde cero")
        self.driver.get("https://chat.openai.com/")
        print("Cargando ChatGPT")

    def chatear(self, prompt):
        """
        Introduce un prompt y devuelve el resultado generado por ChatGPT
        """
        # Introducimos texto en la caja del prompt
        e = self.driver.find_element(By.CSS_SELECTOR, "#prompt-textarea")
        e.send_keys(prompt)

        # Pulsamos en el avioncito de send
        try:
            e = self.driver.find_element(
                By.CSS_SELECTOR, "button[data-testid='send-button']"
            )
            e.click()
            time.sleep(1)
        except:
            print("No se pudo encontrar el botón de enviar")

        # Esperamos a que el botón "Detener la generación" desaparezca
        estado = False
        while not estado:
            estado = esperar_boton_detener_generacion(self.driver)

        # Generamos respuesta
        # Obtener todos los elementos div que contienen respuestas
        elementos_respuesta = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.markdown.prose.w-full.break-words.dark\\:prose-invert.dark",
        )
        # Obtener la respuesta más reciente
        if elementos_respuesta:
            respuest = elementos_respuesta[-1].text
        else:
            respuest = ""

        print(respuest)

        return respuest

    def cerrar(self):
        print("Saliendo....")
        self.driver.quit()


""" Main """
if __name__ == "__main__":
    programa = Programa(user, password)
    # input("pausa")
    while True:
        prompt = input("Introduzca algo: ")

        if prompt.lower() == "cerrar":
            programa.cerrar()
            sys.exit()
        else:
            respuesta = programa.chatear(prompt=prompt)
