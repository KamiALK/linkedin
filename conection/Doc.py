
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
print(type(document_content)) #list

#ubicacion de los index de los content
def extract_text_from_document(document_content):
    text = ""
    index = 0
    diccionario = {}
    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element:
                    text += element['textRun']['content']
                    index += 1
                    diccionario[index] = element['textRun']['content']
    return text
document_text = extract_text_from_document(document_content)
# print(document_text)




#ubicacion de los index de los content
def marcacion_con_index(document_content):
    text = ""
    index = 0
    diccionario = {}
    # document_apdated = 
    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element:
                    text += element['textRun']['content']
                    index += 1
                    diccionario[index] = element['textRun']['content']
    return diccionario
document_text = marcacion_con_index(document_content)
# print(document_text)



# organicemos los put
def cambiar_valor(diccionario, clave, valor):
    diccionario[clave] = valor

def actualizar_contenido(document_content, updated_content):
    if document_content is None:
        print("El contenido del documento está vacío.")
        return
    
    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element:
                    index = element['startIndex']
                    if index in updated_content:
                        element['textRun']['content'] = updated_content[index]
    
    return document_content

updated_content = cambiar_valor(document_text, 1, 'jeison almanza')
documento_actualizado = actualizar_contenido(document_content, updated_content)

# Enviar la solicitud de actualización al servidor de Google Docs
# service.documents().batchUpdate(documentId=document_id, body={'requests': []}).execute()


# organicemos los put
# def cambiar_valor(diccionario, clave, valor):
#     diccionario[clave] = valor

# updated_content = cambiar_valor(document_text, 1, 'jeison almanza')

# Enviar la solicitud de actualización al servidor de Google Docs
# service.documents().batchUpdate(documentId=document_id, body={'requests': []}).execute()

