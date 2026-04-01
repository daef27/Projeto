import os
import sys

# Adiciona a raiz do projeto
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "associacao.settings")

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()