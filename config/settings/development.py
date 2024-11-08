from .base import *  # noqa

DEBUG = True
SECRET_KEY = "s8pf2=e9)hz9rekd3#w!6el2o-lxb08=yu=$ru9_1!bx083#xd"

ALLOWED_HOSTS = ["*"]

DEV_APPS = ["debug_toolbar"]

DEV_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "mysql.connector.django",
        "NAME": os.getenv("DB_NAME", "wallet_db"),
        "USER": os.getenv("DB_USER", "wallet_user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "7h_8dA2o3gd"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "3306"),
    },
}

INSTALLED_APPS += DEV_APPS
MIDDLEWARE += DEV_MIDDLEWARE
