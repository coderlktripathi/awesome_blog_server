import os


def env(variable, fallback_value=None):
    env_value = os.environ.get(variable)
    if env_value is None:
        return fallback_value
    # Next isn't needed anymore
    elif env_value == "__EMPTY__":
        return ''
    else:
        return env_value


IF_MATCH = True
SECRET_KEY = env('SECRET_KEY', '')
INSTALLED_APPS = ['auth']

CACHE_CONTROL = 'max-age=0, no-cache'

X_DOMAINS = '*'
X_MAX_AGE = 24 * 3600
X_HEADERS = ['Content-Type', 'Authorization', 'If-Match']

#: mongo db name, only used when mongo_uri is not set
MONGO_DBNAME = env('MONGO_DBNAME', 'awesome-blog')

#: full mongodb connection uri, overrides ``MONGO_DBNAME`` if set
MONGO_URI = env('MONGO_URI', 'mongodb://localhost/%s' % MONGO_DBNAME)

#: allow all mongo queries
MONGO_QUERY_BLACKLIST = []

DOMAIN = {}

# NOTE: no trailing slash for the URL setting!
URL = env('URL', 'http://localhost:5500')
MEDIA_PREFIX = env('MEDIA_PREFIX', '%s/assets' % URL.rstrip('/'))
URL_PREFIX = env('URL_PREFIX', 'api')
# API_VERSION = 'v1'

# date formats
DATE_FORMAT = '%Y-%m-%dT%H:%M:%S+0000'

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

XML = False
