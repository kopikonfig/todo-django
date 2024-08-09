# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\konoha\asgi.py

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'konoha.settings')

application = get_asgi_application()
