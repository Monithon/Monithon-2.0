"""
Django settings for monithon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v$y^@7cjg-+fb$p)qad1!y*zy2+c97^!yu22b8=ilvh3t8^_h-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'customforms',
    'reports',
    'projects',
    'social.apps.django_app.default',
    'oauth2_provider',
    'monitor',
    #'south',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'monithon.urls'

WSGI_APPLICATION = 'monithon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': "monithon"  ,
        'USER':"postgres",
        'PASSWORD':''
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = ( 
        os.path.join("/var/www/monithon/Monithon-2.0/monithon/templates"),
    )

AUTHENTICATION_BACKENDS = (
      'social.backends.open_id.OpenIdAuth',
      #'social.backends.google.GoogleOpenId',
      #'social.backends.google.GoogleOAuth2',
      #'social.backends.google.GoogleOAuth',
      'social.backends.facebook.Facebook2OAuth2',
      'social.backends.twitter.TwitterOAuth',
      'social.backends.github.GithubOAuth2',
      'django.contrib.auth.backends.ModelBackend',
  )


SOCIAL_AUTH_FACEBOOK_KEY = '728323867229355'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f3ddc23b0cd3d747a921afae31879324'

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_GITHUB_KEY = 'b147309bc240696a0724'
SOCIAL_AUTH_GITHUB_SECRET = 'a4ff2504098c75f908e91290640f012da7a12629'

SOCIAL_AUTH_GOOGLE_OAUTH_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH_SECRET = ''

SOCIAL_AUTH_TWITTER_KEY = 'KdSYuRsed43W1wFrFLpzSMAsL'
SOCIAL_AUTH_TWITTER_SECRET = 'ZD50FfvwYuyqzJKAKfipGNw4P1MqgdV67LzBE90FctswiAY4f3'


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "projects.processor.request",
)