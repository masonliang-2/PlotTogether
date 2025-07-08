# Django settings for project.
# Environment settings, app config, DB setup, and middleware

# Built-in
import os
from pathlib import Path

# Third party
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent     #Finds out where the project lives

load_dotenv()  # Loads .env file into os.environ

### Core Django Settings ###

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")    # SECRET_KEY: required for Django cryptographic signing

# SECURITY WARNING: don't run with debug turned on in production! (set via .env)
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'     #DEBUG: Shows errors in dev

#ALLOWED_HOSTS: What domains/IP's are allowed to access the server
ALLOWED_HOSTS = [       
    'localhost', '127.0.0.1', '[::1]',
    'stormforge-web-774393089590.us-west1.run.app',
    'stormforge-frontend-774393089590.us-west1.run.app',
    ]


## Application definition ##

#INSTALLED_APPS: Django components or third party apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'api',  #loads api/apps.py
]

#MIDDLEWARE: Request/response hooks that Django uses globally
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

#Tells Django which file defines URL routes (stormforge/urls.py)
ROOT_URLCONF = 'stormforge.urls'

#Tells Django which file to use as WSGI for deployment (stormforge/wsgi.py)
WSGI_APPLICATION = 'stormforge.wsgi.application'

#Tells Django how to load HTML templates using render()
    #Ie. controls which (like global) variables are available by default to every template (like HTML files)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',   #Adds 'debug' context if DEBUG = True
                'django.template.context_processors.request',  #Adds the current HttpRequest as 'request'
                'django.contrib.auth.context_processors.auth',  #Adds 'user', 'perms' for authentication
                'django.contrib.messages.context_processors.messages',  #Adds flash messages (via Django's message framework)
            ],
        },
    },
]

# Database
# Tells Django how to connect to your database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}


# Password validation
# Tells Django how to validate passwords for authentication purposes

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# Ensure that the static files are collected

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CORS_ALLOWED_ORIGINS: What frontend URL's can talk to your API
#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:3000",
#    'http://stormforge-web-774393089590.us-west1.run.app',
#    'http://stormforge-frontend-774393089590.us-west1.run.app',
#]

# Optionally, allow all origins (for development purposes only)
CORS_ALLOW_ALL_ORIGINS = True
