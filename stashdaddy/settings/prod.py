# import S3
from .base import *


# AWS credentials
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']

# S3 storage
INSTALLED_APPS.append('storages')
# STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = COMPRESS_STORAGE = 'mystorage.CachedS3StaticStorage'
# AWS_CALLING_FORMAT = S3.CallingFormat.SUBDOMAIN
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY, AWS_EXPIREY)}
STATIC_URL = 'https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

DEBUG = True

COMPRESS_OFFLINE = True
