# sales_inventory_system/settings.py

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# CORRECTED: The first argument of os.environ.get() should be the ENVIRONMENT VARIABLE NAME ('DJANGO_SECRET_KEY').
# The second argument is the fallback value for local development.
# The key 'django-insecure-f^v#j&5g5&i3yv(4a!^w0%m^70-13_a@65q^n7=vj1d&!s!h^r' is your original Django-generated key.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-f^v#j&5g5&i3yv(4a!^w0%m^70-13_a@65q^n7=vj1d&!s!h^r')

# SECURITY WARNING: don't run with debug turned on in production!
# CORRECTED: Set to False for production deployment.
DEBUG = False

# CORRECTED: ALLOWED_HOSTS should only contain hostnames (domain names), not full URLs.
# Added '.' for local development convenience.
ALLOWED_HOSTS = ['Anony123.pythonanywhere.com', '127.0.0.1', '.']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'sales_inventory_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core', 'templates')],
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

WSGI_APPLICATION = 'sales_inventory_system.wsgi.application'


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core', 'static')
]

# CRITICAL FIX: This setting is required for `collectstatic` to know where to put files,
# and for PythonAnywhere to serve them in production.
# This should match the 'Path' you set for static files on PythonAnywhere's Web tab:
# /home/Anony123/Orlantech_Inventory/staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication Redirect URLs
# CORRECTED: Removed duplicate definitions. The last definition takes precedence.
LOGIN_REDIRECT_URL = '/'  # Redirects to the home page after successful login
LOGOUT_REDIRECT_URL = '/' # Redirects to the home page after successful logout
LOGIN_URL = 'login'       # URL for the login page