from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Configuración del navegador
opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=opts
)

# URL de la página de LinkedIn
url = "https://www.linkedin.com/jobs/search/?currentJobId=3903380739&distance=25&geoId=100876405&keywords=analista%20de%20datos&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true"

# Navegar a la página de LinkedIn
driver.get(url)

# Esperar a que la página cargue
time.sleep(5)  # Ajusta el tiempo según la velocidad de tu conexión

# Inicializar el contador de trabajos
contador_trabajos = 0

# Realizar el desplazamiento de la página para cargar más trabajos
while True:
    # Simular el desplazamiento hacia abajo
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)  # Esperar un poco para que se carguen los nuevos elementos

    job_elements = driver.find_elements(By.CSS_SELECTOR, "div.base-card")
    job_ids = [
        job.get_attribute("data-entity-urn").split(":")[3] for job in job_elements
    ]
    trabajos_antes = len(job_ids)
    print(trabajos_antes)
    # Verificar si hay un botón "Ver más empleos" visible
    try:
        ver_mas_empleos_button = driver.find_element(
            By.XPATH, "//button[@aria-label='Ver más empleos']"
        )
    except NoSuchElementException:
        break  # Salir del bucle si no hay más botones "Ver más empleos"

    # Hacer clic en el botón "Ver más empleos"
    try:
        ver_mas_empleos_button.click()
    except ElementNotInteractableException:
        # Si no se puede hacer clic, hacer más desplazamiento hacia abajo y luego continuar
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Esperar un poco después de desplazarse hacia abajo
        continue

    time.sleep(
        2
    )  # Esperar un poco después de hacer clic para que se carguen los nuevos trabajos

    # Obtener los IDs de los trabajos
    job_elements = driver.find_elements(By.CSS_SELECTOR, "div.base-card")
    job_ids = [
        job.get_attribute("data-entity-urn").split(":")[3] for job in job_elements
    ]
    trabajos_despues = len(job_ids)
    if trabajos_despues <= trabajos_antes:
        break
    print(trabajos_despues)
#
# # Imprimir los IDs de los trabajos
# for job_id in job_ids:
#     contador_trabajos += 1
#     print(contador_trabajos, ":", job_id)
#
# Cerrar el navegador
driver.quit()

# Initialize an empty list to store job information
job_list = []

# Loop through the list of job IDs and get each URL
for job_id in job_ids:
    # Construct the URL for each job using the job ID
    job_url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job_id}"
    try:
        # Send a GET request to the job URL and parse the reponse
        job_response = requests.get(job_url)
        # print(job_response.status_code)
        job_soup = BeautifulSoup(job_response.text, "html.parser")
    except:
        print("camilo estuvo aqui")
    # Create a dictionary to store job details
    job_post = {}

    job_post["id_oferta"] = job_id
    # Try to extract and store the job title
    try:
        job_post["job_title"] = job_soup.find(
            "h2",
            {
                "class": "top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title"
            },
        ).text.strip()
    except:
        job_post["job_title"] = None

    # Try to extract and store the company name
    try:
        job_post["company_name"] = job_soup.find(
            "a", {"class": "topcard__org-name-link topcard__flavor--black-link"}
        ).text.strip()
    except:
        job_post["company_name"] = None

    # Try to extract and store the time posted
    try:
        job_post["time_posted"] = job_soup.find(
            "span", {"class": "posted-time-ago__text topcard__flavor--metadata"}
        ).text.strip()
    except:
        job_post["time_posted"] = None

    # Try to extract and store the number of applicants
    try:
        job_post["num_applicants"] = job_soup.find(
            "span",
            {
                "class": "num-applicants__caption topcard__flavor--metadata topcard__flavor--bullet"
            },
        ).text.strip()
    except:
        job_post["num_applicants"] = None

    # Try to extract and store the job description
    try:
        job_description_section = job_soup.find(
            "div", {"class": "show-more-less-html__markup"}
        )
        job_description = ""
        if job_description_section:
            for element in job_description_section.find_all(
                ["strong", "ul", "li", "br"]
            ):
                if element.name == "br":
                    job_description += "\n"
                else:
                    job_description += element.get_text(strip=True) + " "
        job_post["job_description"] = job_description.strip()
    except:
        job_post["job_description"] = None

    # Append the job details to the job_list
    job_list.append(job_post)
# print(job_list)

jobs_df = pd.DataFrame(job_list)
# print(jobs_df)
# Save the DataFrame to a CSV file
try:
    jobs_df.to_csv("vacantes.csv", index=False)
    print("Datos guardados en vacantes.csv")
except Exception as e:
    print(f"Error al guardar los datos en vacantes.csv: {e}")
