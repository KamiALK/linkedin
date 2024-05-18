# hola
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
google_service_account_email = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
google_private_key = os.getenv("GOOGLE_PRIVATE_KEY")

# Ahora puedes usar estas variables en tu código
print("Email de la cuenta de servicio de Google:", google_service_account_email)
print("Clave privada de Google:", google_private_key)
