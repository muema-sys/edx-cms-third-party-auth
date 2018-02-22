from django.conf import settings
from path import Path as path


def add_locale_path():
    settings.MAKO_TEMPLATES['main'].insert(0, path(__file__).abspath().dirname() / 'templates')
