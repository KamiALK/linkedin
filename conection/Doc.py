
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
print(document_content)
print("hola mundo") 
#
# def extract_text_from_document(document_content):
#     text = ""
#     for content in document_content:
#         if 'paragraph' in content:
#             for element in content['paragraph']['elements']:
#                 if 'textRun' in element:
#                     text += element['textRun']['content']
#         elif 'table' in content:
#             for row in content['table']['tableRows']:
#                 for cell in row['tableCells']:
#                     for element in cell['content']:
#                         if 'textRun' in element['paragraph']['elements'][0]:
#                             text += element['paragraph']['elements'][0]['textRun']['content']
#     return text

# Utilizar la función para extraer el texto del documento
# document_text = extract_text_from_document(document_content)

# Imprimir el texto extraído
# print('Texto del documento:')
# print(document_text)


import json
print(document_content)

analisis = json.loads(document_content)
# Modificar el contenido del primer párrafo
documento[1]['paragraph']['elements'][0]['textRun']['content'] = "Nuevo contenido"
# Convertir de nuevo a JSON
documento_modificado = json.dumps(documento)

# Guardar el JSON modificado en un archivo
with open('documento_modificado.json', 'w') as archivo:
    archivo.write(documento_modificado)

