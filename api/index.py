import os
import sys

# Adiciona raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

from django.core.wsgi import get_wsgi_application

# Cria a aplicação WSGI que o Vercel vai usar
app = get_wsgi_application()