# -*- coding: utf-8 -*-
"""
GuitarSocieties.org
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2014 Christopher Davis <http://christopherdavis.me>
:license: http://opensource.org/licenses/bsd-3-clause
"""

import os
import os.path as path
import dj_database_url

os.environ.setdefault('DATABASE_URL', 'postgres://localhost/cgbnext')
os.environ.setdefault('CGS_SECRET', 'h2q2#l6=3eos8a+m_v9n7u%bqwvsljomjp36yh!vy$vf^w-bpp')
os.environ.setdefault('CGS_DEBUG', '1')

BASE_DIR = path.dirname(path.dirname(__file__))
PROJECT_DIR = path.abspath(path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('CGS_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'CGS_DEBUG' in os.environ and os.environ['CGS_DEBUG']

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'societies',
    'django_countries',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'website.urls'

WSGI_APPLICATION = 'website.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(),
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    path.join(PROJECT_DIR, 'static'),
)

TEMPLATE_DIRS = (
    path.join(PROJECT_DIR, 'templates'),
)
