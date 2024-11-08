from .base import *  # noqa

DEBUG = True
SECRET_KEY = "s8pf2=e9)hz9rekd3#w!6el2o-lxb08=yu=$ru9_1!bx083#xd"

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db_test.sqlite3"),
    }
}
