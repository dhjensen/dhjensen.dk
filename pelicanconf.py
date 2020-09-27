#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'dhjensen'
SITENAME = 'dhjensen.dk'
SITEURL = ''

PATH = 'content'

THEME = 'pelican-themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites']

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/dhjensen'),
          ('facebook', 'https://facebook.com/dhjensen'),
          ('github', 'https://github.com/dhjensen'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True