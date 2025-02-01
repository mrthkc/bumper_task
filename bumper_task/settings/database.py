# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
from .environment import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': '5432',
    }
}
