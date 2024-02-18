import base64
import json
import requests
from django.conf import settings


def get_api_token() -> str:
    '''
        Returns pikutis api token
    '''
    return settings.PIKUTIS_API_KEY

def call_pdf_api(file_string:str) -> dict:
    '''
        Calls pikutis api and returns response
    '''
    pdf_request:requests.Request = requests.Request('POST', url="https://pikutis.lt/api/generate-pdf/")
    pdf_request.headers = {"Token": get_api_token()}
    pdf_request.data = file_string.encode('utf-8')

    pdf_response:requests.Response = requests.Session().send(pdf_request.prepare())
    return json.loads(pdf_response.content)

def get_pdf_file(pdf_response:dict) -> bytes:
    '''
        Returns pdf file bytes
    '''
    return base64.b64decode(pdf_response['file_bytes_base_64'])