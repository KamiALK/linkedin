#este fallo  tambien
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 


opts=Options()
opts.add_argument("user-agent=Mozilla/115.11.0esr (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.141 ")

#opts.add_argument("--headless")
# Alternativamente:
# driver = webdriver.Chrome(
#     service=Service('./chromedriver'),
#     options=opts
# )
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get('https://www.linkedin.com/jobs/search?keywords=Analista%2BDe%2BDatos&location=colombia&trk=public_jobs_jobs-search-bar_search-submit&currentJobId=3756397640&position=2&pageNum=0')

sleep(3)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Espera un máximo de 10 segundos hasta que el elemento sea visible
cargo_vacante_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h2'))
)

# Extrae y imprime el texto del elemento
cargo_vacante = cargo_vacante_element.text
print(cargo_vacante)
# cargo_vacante_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/section/div[2]/section/div/div[1]/div/h2')
#
# # Extrae y imprime el texto del elemento
# cargo_vacante = cargo_vacante_element.text
# print(cargo_vacante)
#
# # Cierre del navegador
# driver.quit()

