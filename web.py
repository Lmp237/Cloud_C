import pymysql
try:
    import urlparse
except ModuleNotFoundError:
    from urllib import parse as urlparse
import os

urlparse.uses_netloc.append('mysql')

try:
    if 'DATABASES' not in locals():
        DATABASES = {}

    # Ensure default database exists.
    DATABASES['default'] = DATABASES.get('default', {})

    # Update with environment configuration.
    DATABASES['default'].update({
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['MYSQL_ROOT_PASSWORD'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': os.environ['DATABASE_PORT'],
        'ENGINE': 'django.db.backends.mysql'
    })

except Exception:
    print('Unexpected error:', sys.exc_info())


def connection():
    conn = pymysql.connect(host=DATABASES['default']['HOST'],
                           user=DATABASES['default']['USER'],
                           password=DATABASES['default']['PASSWORD'],
                           database=DATABASES['default']['NAME']
                           )
    c = conn.cursor()
    return c, conn
