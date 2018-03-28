#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########################### General Settings ###################################


AUTHOR = u'Phebe Polk'
SITENAME = u'Polka'
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

USE_FOLDER_AS_CATEGORY = True
DEFAULT_DATE_FORMAT = '%a %d %B %Y'
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/phebepolk/','linkedin'),
          ('GitHub', 'https://github.com/polkapolka','github'),
          ('Stack Overflow', 'https://stackoverflow.com/users/4165272/polka','stack-overflow'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

HIDE_SIDEBAR = True

# TAG_URL = 'tags/{slug}.html'
# TAG_SAVE_AS = 'tags/{slug}.html'
# TAGS_URL = 'tags.html'

## Generate archive
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'


# # works with chameleon theme
# MENUITEMS = [
#     ('Home', '/'),
#     ('Contact', [('About Me','category/pages/about.html'),('LinkedIn', 'https://www.linkedin.com/in/phebepolk/'),
#           ('GitHub', 'https://github.com/polkapolka'),
#           ('Stack Overflow', 'https://stackoverflow.com/users/4165272/polka')]),
#     ]


DISPLAY_PAGES_ON_MENU = False

SITELOGO = 'images/favicon.ico'
SITELOGO_SIZE = '24'

HIDE_SITENAME = False

GITHUB_REPO_COUNT = 2

ADDTHIS_FACEBOOK_LIKE = False
ADDTHIS_GOOGLE_PLUSONE = False
ADDTHIS_TWEET = False

#ABOUT_ME = "Words Go Here."

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


# #BOOTSTRAP_NAVBAR_INVERSE = True ## for inversing colors at navbar
# GITHUB_USER = 'polkapolka'  ## just put your github username here.
# GITHUB_SKIP_FORK = True

FOOTER_INSERT_HTML = '<div class="footer-social"><span>Connect with us:</span><li><a href="https://www.linkedin.com/in/phebepolk/"><img src="linkedin" /></a></li><li><a href="https://github.com/polkapolka"><img src="github" /></a></li><li><a href="https://stackoverflow.com/users/4165272/polka"><img src="stack-overflow" /></a></li>'


#DISPLAY_CATEGORIES_ON_SIDEBAR = True

STATIC_PATHS = ['images']

SHOW_SERIES = True

DISPLAY_ARTICLE_INFO_ON_INDEX = False
SHOW_FOOTER=False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PYGMENTS_STYLE = 'monokai'

BOOTSTRAP_THEME = "flatly"

PLUGIN_PATHS = ['./plugins','./pelican-plugins']
PLUGINS = ['ipynb.markup','i18n_subsites','simple_footnotes', 'extract_toc','series','footer_insert']
#,'simple_footnotes', 'extract_toc', 'feed_summary','sitemap',
THEME = "./pelican-themes/pelican-bootstrap3"


FEED_USE_SUMMARY = True
SUMMARY_MAX_LENGTH = 100

