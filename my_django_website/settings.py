

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2k1so@-tg7o38%i7d#qhn%@k(b)y(#6f0c=xkrl#tqs##&5!'

# SECURITY WARNING: don't run with dxebug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True



#ALLOWED_HOSTS = ['djangotutsme.com','www.djangotutsme.com']#add your domain 


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     #'myapp',
   
)

   
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'my_django_website.urls'

WSGI_APPLICATION = 'my_django_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


STATIC_ROOT = os.path.join(BASE_DIR,'static')
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)


STATIC_DIR=os.path.join(BASE_DIR, 'my_django_website', 'static')

STATICFILES_DIRS = (
    STATIC_DIR,
)

if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'my_django_website','templates'),)


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'data.sqlite3') ,
    }
}

DEFAULT_FROM_EMAIL='email@xour_address.com'
EMAIL_HOST='YOUR SMTP'
EMAIL_PORT=25
EMAIL_HOST_USER='WEBMAIL USERNAME'
EMAIL_HOST_PASSWORD='WEBMAIL PASSWORD'


