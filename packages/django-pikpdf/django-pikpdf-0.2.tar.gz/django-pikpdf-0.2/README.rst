============
pikpdf - propper html to pdf generator
============

django-pikpdf is a Django app to generate pdfs from html templates.
This app will capture the html from a template and convert it to a pdf file 
with all styles in tact.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django-pikpdf" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django-pikpdf",
    ]