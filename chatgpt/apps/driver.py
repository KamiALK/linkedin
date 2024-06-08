# para instalar automaticamente chromedriver
from selenium.webdriver.chromium import service
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager


# chromedriver de selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# para modificar las opciones del webdriver de chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=opts
)


def iniciar_chrome():
    # instalamos la ruta de chrome correspondiente
    # ruta = ChromeDriverManager(path="./chromedriver", log_level=0).install()
    """inicia chorme con los parametros indicados y devuelve el driver"""
    options = Options()
    options.add_argument("--headless")
    user_agent = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    options.add_argument(f"user_agent={user_agent}")
    options.add_argument("--desable-web-security")
    options.add_argument("--desable-extensions")
    options.add_argument("--desable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    # options.add_argument("--disable-blink-features=AutomationControled")
    # PARAMETROS PARA OMITIR opciones
    exp_opt = ["enable-automation", "ignore-certificate-errors", "enable-loggins"]
    options.add_experimental_option("excludeSwitches", exp_opt)
    # PREFERNCIAS DE chromedriver
    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # notificaciones: 0=preguntas | 1=permitir | 2=no permitir
        "intl.accept_lenguages": [
            "es-ES",
            "es",
        ],  # para definir el idioma de navegacion
        "credentials_enable_service": False,  # para evitar que google nos pregunte si queremos guardar las credenciales
    }
    options.add_experimental_option("prefs", prefs)
    # s = Service(ruta)
    # s2 = service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s2, options=options)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    return driver


if __name__ == "__main__":
    driver = iniciar_chrome()
    # input("Pulsa ENTER para Salir.")
    url = "https://drmvarshney.com/?page_id=626"
    driver.get(url)
    driver.quit()
