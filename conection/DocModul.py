import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def obtener_servicio_google_docs():
    load_dotenv()

    google_service_account_email = os.getenv("GOOGLE_SERVICE_ACCOUNT_EMAIL")
    google_private_key = os.getenv("GOOGLE_PRIVATE_KEY")
    document_id = os.getenv("GOOGLE_DOCUMENT_ID")
    token = os.getenv("TOKEN_URI")

    credentials = Credentials.from_service_account_info(
        {
            "type": "service_account",
            "client_email": google_service_account_email,
            "private_key": google_private_key.replace("\\n", "\n"),
            "token_uri": token,
        }
    )

    service = build("docs", "v1", credentials=credentials)
    return service


def obtener_contenido_de_documento(service, document_id):
    document = service.documents().get(documentId=document_id).execute()
    document_content = document.get("body").get("content")
    return document_content


def extraer_texto_de_documento(document_content):
    texto = ""
    for content in document_content:
        if "paragraph" in content:
            for element in content["paragraph"]["elements"]:
                if "textRun" in element:
                    texto += element["textRun"]["content"]
        elif "table" in content:
            for row in content["table"]["tableRows"]:
                for cell in row["tableCells"]:
                    for element in cell["content"]:
                        if "textRun" in element["paragraph"]["elements"][0]:
                            texto += element["paragraph"]["elements"][0]["textRun"][
                                "content"
                            ]
    return texto


def texto():
    service = obtener_servicio_google_docs()
    document_id = os.getenv("GOOGLE_DOCUMENT_ID")
    document_content = obtener_contenido_de_documento(service, document_id)
    texto = extraer_texto_de_documento(document_content)
    print(texto)
