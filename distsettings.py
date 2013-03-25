# Django settings for shenmartav project - should be the same for every instance

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_URLCONF = 'shenmartav.urls'

USE_TZ = True
USE_I18N = True
USE_L10N = True

import os, sys
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(PROJECT_PATH, 'apps'))

MEDIA_ROOT = os.path.join(PROJECT_PATH, '..', 'media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATIC_ROOT = os.path.join(PROJECT_PATH, '..', 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
#    'django.contrib.messages.context_processors.messages',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)


MIDDLEWARE_CLASSES = (
    'forcedefaultlanguage.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.toolbar.ToolbarMiddleware',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # File browser has to go before admin
    'filebrowser',

    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.comments',
    'django.contrib.markup',

    # third-party
    'south',
    'reversion',
    'mptt',
    'menus',
    'sekizai',
    'haystack',
    'modeltranslation',
    'sorl.thumbnail',
    'imagekit', # Kind of ugly to have two thumbnail libs, cleanup later
    'rosetta',
    'tinymce',
    'podcasting',
    'licenses',

    # cms
    'cms',
    'cms_search',
    'cms.plugins.file',
    'cms.plugins.link',
    'cms.plugins.picture',
    #'cms.plugins.snippet',
    'cms.plugins.teaser',
    'cms.plugins.text',
    #'cms.plugins.flash',
    #'cms.plugins.googlemap',
    #'cms.plugins.video',
    #'cms.plugins.twitter',

    # mysociety.org
    'popit',
    #'mapit',

    # blog
    'basic.inlines',
    'basic.blog',
    'tagging',
    'markdown',

    # in-house
    'api',
    'representative',
    'votingrecord',
    'incomedeclaration',
    'draftlaw',
    'question',
    'contact',
    'smsregister',
    'smsalert',
)



###########################################################
# testing-related
###########################################################
SOUTH_TESTS_MIGRATE = False
if 'test' in sys.argv:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3'
        }
    }



###########################################################
# login
# after login (which is handled by django.contrib.auth), redirect to the
# dashboard rather than 'accounts/profile' (the default).
###########################################################
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/admin/login'



###########################################################
# logging
#
# the default log settings are very noisy.
###########################################################
LOG_LEVEL = "DEBUG"
LOG_FILE = "log/shenmartav.log"
LOG_FORMAT = "[%(name)s]: %(message)s"
LOG_SIZE = 65536  # 8192 bits = 8 kb
LOG_BACKUPS = 32  # number of logs to keep


###########################################################
# markdown
###########################################################
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_SET = 'markitup/sets/markdown'



###########################################################
# mapit
###########################################################
#MAPIT_AREA_SRID = 27770
#MAPIT_AREA_SRID = 4326
#MAPIT_COUNTRY = 'uk'
#MAPIT_RATE_LIMIT = ()



###########################################################
# CMS
###########################################################
gettext = lambda s: s
CMS_TEMPLATES = (
    ('simple.html', gettext('Simple Template')),
    ('3col.html', gettext('3 Column Template')),
)
CMS_LANGUAGE_CONF = {
    'ka': ['en'],
}
CMS_FRONTEND_LANGUAGES = ('ka', 'en', 'ka')


###########################################################
# TinyMCE
###########################################################
TINYMCE_DEFAULT_CONFIG = {'theme': 'advanced', 
                          'relative_urls': False,
                          'width': '640',
                          'height': '480',}
TINYMCE_FILEBROWSER = True


###########################################################
# haystack
###########################################################
HAYSTACK_SITECONF = 'search_sites'
HAYSTACK_SEARCH_ENGINE = 'xapian'
HAYSTACK_XAPIAN_PATH = os.path.join(PROJECT_PATH, '..', 'xapian_index')
#import xapian
#HAYSTACK_XAPIAN_FLAGS = xapian.QueryParser.FLAG_DEFAULT | xapian.QueryParser.FLAG_PARTIAL
# FIXME: This is a complete hack to get around circular imports in 
# django-haystack and other apps such as django-endless-pagination
SKIP_COMMANDS = ['syncdb', 'migrate', 'schemamigration', 'datamigration', 'reset',
    'import_draftlaws', 'import_incomedeclarations', 'import_representatives',
    'import_votingrecords',
    'update_attendance', 'update_assets', 'update_votingrecordresults',
    'update_votingrecords', 'update_initiators_authors',]
if any([command in sys.argv for command in SKIP_COMMANDS]):
        HAYSTACK_ENABLE_REGISTRATIONS = False



###########################################################
# modeltranslation
###########################################################
MODELTRANSLATION_TRANSLATION_REGISTRY = 'shenmartav.translation'


###########################################################
# rosetta
###########################################################
ROSETTA_MESSAGES_PER_PAGE = 20
ROSETTA_WSGI_AUTO_RELOAD = True
ROSETTA_UWSGI_AUTO_RELOAD = ROSETTA_WSGI_AUTO_RELOAD
#ROSETTA_ENABLE_TRANSLATION_SUGGESTIONS = False
#BING_APP_ID = ''
#ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'en'
#ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'English'
#ROSETTA_EXCLUDED_APPLICATIONS = ()
#ROSETTA_REQUIRES_AUTH = True
#ROSETTA_POFILE_WRAP_WIDTH = 78
#ROSETTA_STORAGE_CLASS = 'rosetta.storage.CacheRosettaStorage'


###########################################################
# Feeds
###########################################################
NUM_FEEDITEMS = 10 # number of items in feed


##########################################################
# base income of representatives, August 2012
##########################################################
BASE_INCOME = {
    'parliament': 24000,
    'tbilisi': 16800,
    'ajara': '23400',
}
