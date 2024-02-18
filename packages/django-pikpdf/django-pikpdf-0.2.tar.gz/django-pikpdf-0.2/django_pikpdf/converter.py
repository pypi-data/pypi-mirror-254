import json
import logging
from django.http import HttpResponse
from .controllers.api import call_pdf_api, get_pdf_file
from .controllers.validators import are_settings_valid
from .controllers.html_transformation import fix_static_urls, fix_media_urls

logger = logging.getLogger(__name__)

def get_document_pdf_response(file_string:str, file_name:str = "document") -> tuple[HttpResponse, bytes]:
    '''
        Returns django http response with pdf file
        and file bytes. File will be named as filename or if not provided: "document.pdf"
    '''
    try:
        file = None
        response = None
        errors:list = []
        errors = are_settings_valid()
        if errors:
            return HttpResponse(json.dumps(errors), status=500), None
        
        file_string = fix_static_urls(file_string)
        file_string = fix_media_urls(file_string)
        
        pdf_response:dict = call_pdf_api(file_string)
        
        if pdf_response["error"]:
            return HttpResponse(pdf_response["error"], status=500), None

        file = get_pdf_file(pdf_response)
        response = HttpResponse(file, content_type='application/pdf')
        response['Content-Disposition'] = f'inline;filename={file_name}.pdf'
        return (response, file)
    
    except Exception as e:
        return HttpResponse(str(e), status=500), None