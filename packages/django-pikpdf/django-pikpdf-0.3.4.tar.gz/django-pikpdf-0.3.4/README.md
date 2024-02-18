
# django-pikpdf - propper html to pdf generator

django-pikpdf is a Django app to generate pdfs from html templates.
This app will capture the html from a template and convert it to a pdf file 
with all styles in tact.

Generator method returns htp responce which you can directly return to screen and file bytes, if you want to attach file to email, or return different response

This generator **does not rely on xhtml2pdf**

Generator uses api on www.pikutis.lt site. No information sent to api is stored longer than required for processing. 

To obtain API key, use contact form in the site.

## Quick start


1. Add "django-pikpdf" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...,
        "django-pikpdf",
    ]

2. Add the following settings to your settings.py:
    
    ```
    PIKUTIS_API_KEY=os.environ.get("PIKUTIS_API_KEY", None) # can be obtained from https://www.pikutis.lt for free
    SITE_URL = os.environ.get("SITE_URL", "https://www.pikutis.lt") # your website url
    
2. Include conversion method get_document_pdf_response as so:

    ```
    from django_pikpdf.utils import get_document_pdf_response

3. Use the method to convert your html to pdf and return a response:

    ```
    html_content = render_to_string("my_template.html", context)
    file_name = "my_pdf_file"
    http_response, file_bytes = get_document_pdf_response(html_content, file_name)
    # HTTP response is a response object which will display pdf in browser screen
    # file_bytes is the pdf file buffer, which you can i.e. attach to email
    return http_response

That's it! You can now convert your html to pdf and return it as a response.