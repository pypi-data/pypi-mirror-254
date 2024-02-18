from django.conf import settings

def fix_static_urls(html:str) -> str:
    """
    Fixes the static urls in the html file
    """
    if settings.DEBUG:
        return html
    return html.replace(settings.STATIC_URL, settings.SITE_URL + settings.STATIC_URL)

def fix_media_urls(html:str) -> str:
    """
    Fixes the media urls in the html file
    """
    if settings.DEBUG:
        return html
    return html.replace(settings.MEDIA_URL, settings.SITE_URL + settings.MEDIA_URL)