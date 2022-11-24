"""
Django settings for eis_root project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from django.contrib import messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-evpaa0n7_xnyiqa*vjf$40i+-_)8wj%t*#eo0^i)xrvdeg1b0p'
RECAPTCHA_PUBLIC_KEY = '6LekXV8eAAAAAIeEKFr58LqcdnQliqsQVU64Zj-e'
RECAPTCHA_PRIVATE_KEY = '6LekXV8eAAAAAMVGefbbbhzU0e7Jm1yTJlq9d92f'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ["https://6093-82-215-100-197.eu.ngrok.io"]

# Application definition
MONTH = [
    (1,'Yanvar'),
    (2,'Fevral'),
    (3,'Mart'),
    (4,'Aprel'),
    (5,'May'),
    (6,'Iyun'),
    (7,'Iyul'),
    (8,'Avgust'),
    (9,'Sentyabr'),
    (10,'Oktyabr'),
    (11,'Noyabr'),
    (12,'Dekabr'),
]

INSTALLED_APPS = [
    'minenergiya',
    'kirish','s_ad', 'foydalanuvchi',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'crispy_forms',
    'phonenumber_field',
    
]

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    
    'django.middleware.common.CommonMiddleware',    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eis_root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eis_root.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'eis_root/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = os.path.join(BASE_DIR, 'eis_root/media')
MEDIA_URL = '/media/'

#messages lar
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    messages.WARNING: 'warning'    
}

# email stuff *************************************************************
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'nurbek.kurbonov.96@gmail.com'
EMAIL_HOST_PASSWORD = 'zdkkebohyiulpzrn'
EMAIL_PORT = 587

#additional -***************************************************************
LOGIN_URL='/login/'
#AUTH_USER_MODEL = 'kirish.CustomUser'
