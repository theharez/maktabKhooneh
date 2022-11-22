from main.settings import *


SECRET_KEY = 'django-insecure-@3f9047ghu#2ae6o&f4&l)w7qn2(-7q@%8+g+yo^bx9s!(6n98'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR/'assets',
]

CSRF_COOKIE_SECURE = True 