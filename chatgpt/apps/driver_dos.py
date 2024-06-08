from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome import service as serv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
from shutil import which


def Iniciar_driver(headless=True):
    """arranca webdriver con chrome y lo devuelve"""
    options = Options()
    if headless:
        options.add_argument("--headless")
        options.add_argument("--window-size=1360,758")
        options.add_argument("--start-maximized")
        options.add_argument(
            "--disable-dev-shm-usage"
        )  # para usar un directorio temporal para crear archivos anonimos de uso compartido
        options.add_argument("--log-level=1")  # para que no muestre nada en la terminal
        lista = [
            "enble-automation",  # para ocultar mensaje de pruebas automatizados
            "enable-loggin",  # para ocultar dev tools
        ]
        options.add_experimental_option("excludeSwitches", lista)
        s = Service(which("chromedriver"))
        driver = webdriver.Chrome(service=s, options=options)
        stealth(
            driver,
            languages=["es-Es", "es"],
            vendor="Google Inc.",
            platform="win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )
    print("hola mundo")
    return driver
