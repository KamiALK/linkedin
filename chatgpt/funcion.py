# modulos de terceros
from selenium.webdriver.common.by import By  # para buscar por tipos de elemento
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys  # para pulsar teclas especiales
from selenium.webdriver.support.ui import WebDriverWait  # para esperar en selenium
from selenium.common.exceptions import TimeoutException


def esperar_boton_detener_generacion(driver, primera_vez=False):
    """
    Espera a que aparezca el botón con el data-testid "send-button",
    omitiendo la espera si ya está presente desde el inicio.
    """
    try:
        # Esperamos a que aparezca el botón
        wait = WebDriverWait(driver, 200)
        boton_enviar = wait.until(
            ec.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "button[data-testid='send-button']",
                )
            )
        )
        print("holala ")

        return True

    except TimeoutException:
        # El botón no ha sido encontrado dentro del tiempo especificado
        print("El botón 'Enviar' no ha aparecido dentro del tiempo especificado")
        return False
