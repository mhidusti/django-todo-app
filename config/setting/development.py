from config.settings import *


SECRET_KEY = (
    "django-insecure-bqauw9i_skvc58&j3ksgio50t+lv^u7kb-a@t1gnotv%^5yq)c"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# if DEBUG:
#     import socket  # only if you haven't already imported this

#     hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
#     INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + [
#         "127.0.0.1",
#         "172.27.0.2",
#     ]
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR.joinpath("/static")
MEDIA_ROOT = BASE_DIR.joinpath("media/")

STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "media",
]

