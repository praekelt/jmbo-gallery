from os.path import expanduser

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jmbo',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'gallery',
    'jmbo',
    'photologue',
    'category',
    'likes',
    'secretballot',
    'publisher',
    'pagination',
    'layers',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'south',
)

ROOT_URLCONF = 'gallery.tests.urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'likes.middleware.SecretBallotUserIpUseragentMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'

CKEDITOR_UPLOAD_PATH = expanduser('~')

SOUTH_TESTS_MIGRATE = False

# Disable celery
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'

# To test layers we need these settings
LAYERS = {'layers': ['basic']}

TEMPLATE_LOADERS = (
    'layers.loaders.filesystem.Loader',
    'django.template.loaders.filesystem.Loader',
    'layers.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    'layers.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'layers.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
