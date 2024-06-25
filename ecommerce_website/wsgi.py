"""
WSGI config for ecommerce_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_website.settings") #要上傳到render，此處名稱要對應到檔案"Procfile"。#檔案"Procfile"：要上傳到render，此處名稱要對應到"wsgi.py"

application = get_wsgi_application()
