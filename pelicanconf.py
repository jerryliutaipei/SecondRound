#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chiu CC'
SITENAME = u'Ordinary Days'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True
USE_FOLDER_AS_CATEGORY = True

# Theme
THEME = 'theme/Flex'

# Static path
STATIC_PATHS = [('fig'),]

# Flex setting
SITETITLE = SITENAME
SITESUBTITLE = u'Hey'
SITEDESCRIPTION = u'Not Bad Not Bed'
SITELOGO = u'https://alrightchiu.github.io/SecondRound/content/fig/antiwar.jpg'

MENUITEMS = [
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
]

# Blogroll
LINKS = (
 	('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)


# Social widget
SOCIAL = (
	('You can add links in your config file', '#'),
    ('Another social link', '#'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
