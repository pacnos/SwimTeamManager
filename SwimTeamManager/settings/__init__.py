import os

import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TeamManager',
    'AdminBackend'
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

ROOT_URLCONF = 'SwimTeamManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')]
        ,
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

WSGI_APPLICATION = 'SwimTeamManager.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Logger Settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'log_to_stdout': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            },
        },
    'loggers': {
        'django': {
            'handlers': ['log_to_stdout'],
            'level': 'DEBUG',
            'propagate': True,
            }
        }
    }


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "../translations")
]

# Default urls
LOGIN_REDIRECT_URL = "dashboard"
LOGIN_URL = "login"
LOGOUT_REDIRECT_URL = "login"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../static")
]
STATIC_ROOT = os.path.join(BASE_DIR, "../static_deploy")

# Application Settings
######################

# Warning times
MEDICAL_WARN_TIME = 3 * 30
SECOND_MEDICAL_WARN_TIME = 30

# Date formats
IMPORT_DATE_FORMAT = "%Y-%m-%d"



# DEBUG IMPORT
from SwimTeamManager.settings.debug import *
# PRODUCTION IMPORT
# from SwimTeamManager.settings.production import *