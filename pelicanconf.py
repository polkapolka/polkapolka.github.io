#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

########################### General Settings ###################################


AUTHOR = u'Phebe Polk'
SITENAME = u'Phebe Polk'
SITEURL = ''

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = True

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# USE_FOLDER_AS_CATEGORY = True
# DEFAULT_DATE_FORMAT = '%a %d %B %Y'
# DEFAULT_DATE = 'fs'

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
#RELATIVE_URLS = True

# ARTICLE_URL = '{category}/{slug}/'
# ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
# PAGE_URL = '{slug}.html'
# PAGE_SAVE_AS = '{slug}.html'
# TAG_URL = 'tags/{slug}.html'
# TAG_SAVE_AS = 'tags/{slug}.html'
# TAGS_URL = 'tags.html'

## Generate archive
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

ABOUT_ME = "Words Go Here."

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PYGMENTS_STYLE = 'monokai'

BOOTSTRAP_THEME = "Flatly"

PLUGIN_PATHS = ['./plugins','./pelican-plugins']
PLUGINS = ['ipynb.markup','i18n_subsites','autopages']
#,'simple_footnotes', 'extract_toc', 'feed_summary','sitemap',
THEME = "./pelican-themes/pelican-bootstrap3"

# AUTHOR_PAGE_PATH = './content/authors/author.md'

# FEED_USE_SUMMARY = True
# SUMMARY_MAX_LENGTH = 100

# MD_EXTENSIONS = ['toc', 'fenced_code', 'codehilite(css_class=highlight)', 'extra']
