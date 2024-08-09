# E:\bin django\KORPS POLISI MILITER\SESPIM POLRI\konoha\konoha\wsgi.py

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'konoha.settings')

application = get_wsgi_application()
