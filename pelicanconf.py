#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'admin'
SITENAME = u'Shiloh Presbyterian Church'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['./static']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (,)

# Social widget
# SOCIAL = (,)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = './pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites', 'assets']
WEBASSETS = True
BOOTSTRAP_FLUID = False


CUSTOM_CSS = 'static/custom.css'

# Navbar
SITELOGO = 'static/logo.jpg'
HIDE_SITENAME = True

# Body
HIDE_SIDEBAR = True
BANNER = 'static/skyline_20.jpg'