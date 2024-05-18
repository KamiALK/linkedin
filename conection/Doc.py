
import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener las variables de entorno
google_service_account_email = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
google_private_key = os.getenv("GOOGLE_PRIVATE_KEY")
document_id = os.getenv('GOOGLE_DOCUMENT_ID')
token = os.getenv('TOKEN_URI')

# Crear las credenciales
credentials = Credentials.from_service_account_info({
    'type': 'service_account',
    'client_email': google_service_account_email,
    'private_key': google_private_key.replace('\\n', '\n'),
    'token_uri': token
})

# Construir el servicio de Google Docs
service = build('docs', 'v1', credentials=credentials)

# Obtener el contenido del documento
document = service.documents().get(documentId=document_id).execute()
document_content = document.get('body').get('content')

# Imprimir el contenido del documento
print('Contenido del documento:')
print(document_content)
