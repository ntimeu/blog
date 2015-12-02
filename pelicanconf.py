#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ntimeu'
SITENAME = "NTimeu's blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Articles configuration
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}.html'

PAGE_URL = 'pages/{number}.html'
PAGE_SAVE_AS = 'pages/{number}.html'

CATEGORY_URL = 'categories/{slug}.html'
CATEGORY_SAVE_AS = 'categories/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
ARCHIVES_URL = 'archives.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
FEED_MAX_ITEMS = 50

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['liquid_tags.include_code']

# Theme
THEME = 'blue-penguin'
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True

MENU_INTERNAL_PAGES = (
    ('Archives', ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

MENUITEMS = (
    ('GitHub', 'https://github.com/ntimeu'),
    ('Bitbucket', 'https://bitbucket.org/ntimeu'),
    ('Links', 'http://links.ntimeu.fr/'),
)
