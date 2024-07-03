import undetected_chromedriver as uc


def Iniciar_driver(pos="maximizada"):
    """Inicia un navegador Chrome y devuelve el objeto WebDriver instanciado"""
    # Instanciamos las opciones de Chrome
    options = uc.ChromeOptions()
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    # Configuramos la opción headless dentro de ChromeOptions
    options.headless = (
        False  # Cambiar a True si se desea iniciar el navegador en modo headless
    )

    # Iniciamos el driver
    driver = uc.Chrome(
        options=options,
        log_level=3,
    )
    # Posicionamos la ventana según corresponda
    if pos != "maximizada":
        # Obtenemos la resolución de la ventana
        ancho, alto = driver.get_window_size().values()
        driver.set_window_rect(x=0, y=0, width=ancho // 2, height=alto)
    return driver
