from pathlib import Path

# SECURITY WARNING: keep the secret key used in production secret!
mySECRET_KEY = 'django-insecure-5mr2lr1_wtv1^m47t9@x)=&1u*yypv7exeise4@df$swq5skiv'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

BASE_DIR = Path(__file__).resolve().parent.parent

myDATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysql',
        'USER' : 'root',
        'PASSWORD':'12345',
        'HOST': '127.0.0.1',
        'PORT':'3306',
    }
}