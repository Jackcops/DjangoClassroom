from .settings import *

# run manage.py with --settings=main.settings_prod

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'dj_mysql',
        'PORT': '3306',
    }
}


ALLOWED_HOSTS = ["wd0303.coe.psu.ac.th"]
CSRF_TRUSTED_ORIGINS = ["https://wd0303.coe.psu.ac.th"]


DEBUG = True