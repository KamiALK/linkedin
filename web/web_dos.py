#este fallo
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager 

# Configurar las opciones del navegador
opts = Options()
opts.add_argument("user-agent=Mozilla/115.11.0esr (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.141 ")

# Inicializar el driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

# Navegar a la página
driver.get('https://www.linkedin.com/jobs/search?keywords=data%2Bscience&location=Bogota%2C%2BNueva%2BJersey%2C%2BEstados%2BUnidos&geoId=107150092&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3908699150&position=3&pageNum=0')

# Esperar a que el div con clase 't-24' esté presente
div_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "t-24"))
)

# Encontrar el h1 dentro del div
h1_element = div_element.find_element(By.CLASS_NAME, "t-24 t-bold inline")

# Obtener el texto del h1
h1_text = h1_element.text
print(h1_text)

# Cerrar el navegador
driver.quit()
