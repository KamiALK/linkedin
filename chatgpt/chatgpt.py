# moldulos de python
import os
import sys
import time
import pickle
import tempfile


# modulos de terceros
from selenium.webdriver.common.by import By  # para buscar por tipos de elemento
from selenium.webdriver.support import (
    expected_conditions as ec,
)  # para condiciones en selenium
from selenium.webdriver.common.keys import Keys  # para pulsar teclas especiales
from selenium.webdriver.support.ui import WebDriverWait  # para esperar en selenium

# propios
from apps.oculto import Iniciar_driver


class ChatGpt:
    def __init__(self, user, password):
        """
        iniciamos  webdriver y nos logueamos en ChatGpt
        """
        self.OPENAI_USER = user
        self.OPENAI_PASS = password
        self.COOKIES_FILE = f"{tempfile.gettempdir()}/openai.cookies"
        self.driver = Iniciar_driver(pos="izquierda")
        self.wait = WebDriverWait(self.driver, 30)
        login = self.login_openai()
