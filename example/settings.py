#-*- coding: utf-8 -*-
import os, sys
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
sys.path.insert(0,  os.path.join(PROJECT_PATH, '..'))

ADMIN_MEDIA_PREFIX = '/admin_media/'
DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'example.db'
DEBUG = True
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'debug_toolbar',
    #'django_extensions',
)
INTERNAL_IPS = ('127.0.0.1',)
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
ROOT_URLCONF = 'example.urls'
SECRET_KEY = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd'
SITE_ID = 1
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (os.path.join(PROJECT_PATH, 'templates'))

from debug_toolbar.utils.debug_cmd import DebugCmd
from debug_toolbar.utils.commands import force_login_admin, force_logout

DEBUG_CMD_FUNCTIONS = (
        DebugCmd('login_admin', 'Enter as admin', force_login_admin),
        DebugCmd('logout', 'Logout', force_logout),
        )
# left it for easier function search
DEBUG_CMD_FUNCTIONS = dict(((debug_cmd.name, debug_cmd) for debug_cmd in DEBUG_CMD_FUNCTIONS)) 
