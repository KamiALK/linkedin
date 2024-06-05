
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
# print(document_content)


def extract_text_from_document(document_content):
    text = ""
    contador = 1
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
                            
    # print(contador)
    return text

# Utilizar la función para extraer el texto del documento
document_text = extract_text_from_document(document_content)

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
dic = crear_diccionario_contenido(document_content)
dic_dos = crear_diccionario_contenido(document_content)
# print(diccionario)

def imprimir_diccionario(diccionario):
    for clave, valor in diccionario.items():
        print(f"{clave}: {valor}")
        # print()  # Agrega un salto de línea después de cada clave

# Ejemplo de uso:
# imprimir_diccionario(diccionario)

# nuevo_valor=input(str("ingrese valor nuevo: "))
# dic_dos[1]=nuevo_valor



# Crear la solicitud de actualización por lotes
class DocumentUpdater:
    def __init__(self):
        self.solicitudes = []

    def add(self, valor_viejo, valor_nuevo):
        solicitud = {
            'replaceAllText': {
                'replaceText': valor_nuevo,
                'containsText': {
                    'text': valor_viejo,
                    'matchCase': True
                }
            }
        }
        self.solicitudes.append(solicitud)

    def get_solicitudes(self):
        return {'requests': self.solicitudes}

def iterar_diccionarios(diccionario_original, diccionario_clon):
    updater = DocumentUpdater()  # Crear una instancia de DocumentUpdater

    for indice, valor_original in diccionario_original.items():
        valor_clon = diccionario_clon[indice]  # Obtener el valor del clon

        updater.add(valor_original, valor_clon)

    solicitud = updater.get_solicitudes()

    return solicitud

solicitud = iterar_diccionarios(dic, dic_dos)

# Uso de la clase DocumentUpdater
# updater = DocumentUpdater()
# updater.add(f'{dic[1]}, f'{dic_dos[1]}')

# updater.add("Desarollador backend", "hola papito")
# Obtener la solicitud generada por la clase
# solicitud = updater.get_solicitudes()
# print(dic[1])
# print(solicitud)

# Ejecutar la solicitud de actualización por lotes
service.documents().batchUpdate(documentId=document_id, body=solicitud).execute()
print('Documento actualizado con éxito.')
