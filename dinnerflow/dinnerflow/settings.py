"""
Django settings for dinnerflow project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m)=-gymt_m&k7p=ly8ka*i^s@685#rucj+hef&s2f1b)mej=n3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "crispy_forms",
    "crispy_bootstrap5",

    'base.apps.BaseConfig',
    'accounts.apps.AccountsConfig',
    'payment.apps.PaymentConfig',
    'menu.apps.MenuConfig',

    'qr_code',
    'paypal.standard.ipn',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dinnerflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'dinnerflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pl-PL'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STRIPE_SECRET_KEY = "sk_test_51P7BXD002G6z9sQo9GJLOOfGP06z9Jrl66GrUx9OSj9l6I3H8ELH981Zpn69y3x26UVURdKLoX0d0Kd4U3yBuwig00S4f1CzPn"
STRIPE_PUBLISHED_KEY = "pk_test_51P7BXD002G6z9sQonDlufMaSg8g54zmeUlCdv2YsCMD6c97iLxKUHGyazCHsmVGSxsdJ4Zviv9Y0Dq0bHxl7opre00AJB4gprv"

#Crispy forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

login_redirect_url = '/'
logout_redirect_url = '/'


PAYPAL_RECEIVER_EMAIL = 'joway92431@acname.com'
# PAYPAL_RECEIVER_EMAIL = 'paypal-facilitator@business.example.com'
PAYPAL_TEST = True
PAYPAL_BUY_BUTTON_IMAGE = 'https://cdn.discordapp.com/attachments/1206894551260991491/1230910541447434290/png-clipart-logo-paypal-graphics-product-computer-icons-paypal-blue-angle-thumbnail-removebg-preview.png?ex=663509c6&is=662294c6&hm=d41bcb2a3fb385aac6b25f7b1b934d7822e049df0e5f1fe764edef2ad80f8500&'