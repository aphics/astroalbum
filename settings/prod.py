from .base import *
import pymysql


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.version_info = (1, 4, 2, 'final', 0)

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name_DB',
        'USER': 'user_DB',
        'PASSWORD': 'password_DB',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}