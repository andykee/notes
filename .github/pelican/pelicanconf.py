import datetime

AUTHOR = 'Andy Kee'
SITENAME = 'AK Notes'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

THEME = "theme"

YEAR = datetime.datetime.now().year

PLUGINS = [
    "pelican.plugins.render_math", # https://github.com/pelican-plugins/render-math
]

# Top-level pages tp render
# default is ['index', 'authors', 'categories', 'tags', 'archives']
DIRECT_TEMPLATES = ['index']

# The following lines suppress the generation of individual category and
# author pages
AUTHOR_SAVE_AS = ''
#CATEGORY_SAVE_AS = ''

# If no date metadata is available, grab a timestamp from the system
DEFAULT_DATE = 'fs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True