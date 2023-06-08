import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv
from storages.backends.s3boto3 import S3Boto3Storage
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', '421432')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.apps.AppsConfig',

    # Third party
    'rest_framework',
    'rest_framework_simplejwt',
    # 'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
    'mptt',
    # 'parler',
    'ckeditor_uploader',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('SQL_DATABASE', os.path.join(BASE_DIR, "db.sqlite3")),
        'USER': os.getenv('SQL_USER'),
        'PASSWORD': os.getenv('SQL_PASSWORD'),
        'HOST': os.getenv('SQL_HOST'),
        'PORT': os.getenv('SQL_PORT')
    }
}

# DATABASES = {
#     'default': dj_database_url.config(default=os.getenv('DB_URL', 'postgres://postgres:1@localhost:5432/p8_database'),
#                                       conn_max_age=600,
#                                       conn_health_checks=True, )
#     #     # postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]`
# }

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient"
#         },
#         "KEY_PREFIX": "django"
#     }
# }

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
#
# from django.utils.translation import gettext_lazy as _
#
# PARLER_DEFAULT_LANGUAGE_CODE = 'en'
#
# PARLER_LANGUAGES = {
#     None: (
#         {'code': 'uz', },
#         {'code': 'ru', },
#         {'code': 'en', },
#     ),
#     # 'default': {
#     #     'fallbacks': ['en'],          # defaults to PARLER_DEFAULT_LANGUAGE_CODE
#     #     'hide_untranslated': False,   # the default; let .active_translations() return fallbacks too.
#     # }
# }

# LANGUAGES = (
#     ('uz', _('Uz')),
#     ('ru', _('Ru')),
#     ('en', _('En')),
# )
#
# LANGUAGE_CODE = 'uz'
#
# LOCALE_PATHS = (
#     os.path.join(BASE_DIR, 'locale'),
# )

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = "uploads/"
REST_FRAMEWORK = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication'
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'DATE_INPUT_FORMATS': ["%H:%M %d-%m-%Y"],
    'DATETIME_FORMAT': '%H:%M %d-%m-%Y',
    'DEFAULT_PAGINATION_CLASS': 'apps.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 10,
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle'
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '5/minute',
    #     'user': '10/minute'
    # }
}

# django-storages settings
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

# AWS_ACCESS_KEY_ID = os.getenv("MINIO_ROOT_USER")
# AWS_SECRET_ACCESS_KEY = os.getenv("MINIO_ROOT_PASSWORD")
# AWS_STORAGE_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
# AWS_S3_ENDPOINT_URL = os.getenv("MINIO_END POINT")

#
# AWS_DEFAULT_ACL = None
# AWS_QUERYSTRING_AUTH = True
# AWS_S3_FILE_OVERWRITE = False


CELERY_BROKER_URL = os.getenv('CELERY_BROKER')

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'tasks.add',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }
# app.conf.timezone = 'UTC'


SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        },
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Type in the *\'Value\'* input box below: **\'Bearer &lt;JWT&gt;\'**, '
                           'where JWT is the JSON web token you get back when logging in.'
        }
    }
}


'''

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2MjkzMTU0LCJpYXQiOjE2ODYyMDY3NTQsImp0aSI6ImJlNDIyZTAxN2YwYjQzM2M4ZjQ1MGY2NGY1NmY0OWE0IiwidXNlcl9pZCI6Mn0.ifnEbbE8l6JacMiQiT4RoCowUjY0DnDYiUVdO3QQZCQ

'''

