
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



def extract_text_from_document(document_content):
    text = ""
    contador = 0
    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element:
                    text += element['textRun']['content']
                    contador+=1
        elif 'table' in content:
            for row in content['table']['tableRows']:
                for cell in row['tableCells']:
                    for element in cell['content']:
                        if 'textRun' in element['paragraph']['elements'][0]:
                            text += element['paragraph']['elements'][0]['textRun']['content']
                            contador += 1
                            
    print(contador)
    return text

# Utilizar la función para extraer el texto del documento
document_text = extract_text_from_document(document_content)

# Imprimir el texto extraído
# print('Texto del documento:')
# print(document_text)


def crear_diccionario_contenido(document_text):
    contenido_diccionario = {}
    contador = 1

    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element:
                    contenido_diccionario[contador] = element['textRun']['content']
                    contador += 1

    return contenido_diccionario
diccionario = crear_diccionario_contenido(document_content)
# print(diccionario)

def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
        # print()  # Agrega un salto de línea después de cada clave

# Ejemplo de uso:
# imprimir_diccionario(diccionario)
