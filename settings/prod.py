from .base import *
import pymysql


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['198.199.72.110']


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

pymysql.version_info = (1, 4, 2, 'final', 0)

pymysql.install_as_MySQLdb()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'astroalbum_db',
        'USER': 'aphics',
        'PASSWORD': 'astro',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
