# projeto/settings.py
from pathlib import Path

# ----------------------
# BASE
# ----------------------
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-exemplo123"
DEBUG = True
ALLOWED_HOSTS = ["*"]  # Aceita qualquer host no dev container / Codespaces

# ----------------------
# APPS
# ----------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "socios",  # seu app
]

# ----------------------
# MIDDLEWARE
# ----------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # compressão de static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ----------------------
# URLS
# ----------------------
ROOT_URLCONF = "projeto.urls"

# ----------------------
# TEMPLATES
# ----------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # templates globais
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ----------------------
# WSGI
# ----------------------
WSGI_APPLICATION = "projeto.wsgi.application"

# ----------------------
# DATABASE
# ----------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ----------------------
# STATIC
# ----------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----------------------
# MEDIA
# ----------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ----------------------
# LINGUAGEM / TIMEZONE
# ----------------------
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ----------------------
# LOGIN / LOGOUT
# ----------------------
LOGIN_URL = "/admin/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# ----------------------
# CSRF (Codespaces / Vercel / localhost)
# ----------------------
CSRF_TRUSTED_ORIGINS = [
    "https://solid-space-cod-q7rgp44q5vg5cxw74-8000.app.github.dev",
    "http://localhost:8000",
    "https://localhost:8000",
    "https://*.vercel.app",
]

# ----------------------
# DEFAULT PK
# ----------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"