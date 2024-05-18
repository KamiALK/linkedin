
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

class GoogleDocsConnector:
    def __init__(self, service_account_email, private_key):
        self.credentials = Credentials.from_service_account_info({
            'type': 'service_account',
            'client_email': service_account_email,
            'private_key': private_key.replace('\\n', '\n')
        })
        self.service = build('docs', 'v1', credentials=self.credentials)

    def get_document_content(self, document_id):
        document = self.service.documents().get(documentId=document_id).execute()
        return document.get('body').get('content')

    # Aquí puedes agregar más métodos según tus necesidades, como editar el documento, agregar contenido, etc.
