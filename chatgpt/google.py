from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

# Modulos propios
from apps.oculto import Iniciar_driver

# configuracion ded variables de entorno
from dotenv import load_dotenv
import os


load_dotenv()

user_open = os.getenv("OPENAI_USER")
password = os.getenv("OPENAI_PASSPWORD")

if __name__ == "__main__":
    # Iniciamos webdriver
    driver = Iniciar_driver()
    print(f"{driver}")
    wait = WebDriverWait(driver, 30)
    # Cargamos la página de Google
    driver.get("https://accounts.google.com/")
    # Introducimos el usuario
    e = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='email']")))
    e.send_keys(str(user_open))

    e.send_keys(Keys.ENTER)
    # Introducimos la contraseña
    e = wait.until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "input[type='password']"))
    )
    e.send_keys(str(password))
    e.send_keys(Keys.ENTER)
    input()
