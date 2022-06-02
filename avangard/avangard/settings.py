import os

from dotenv import load_dotenv

load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
CSRF_TRUSTED_ORIGINS = [
    "https://e209-83-220-236-197.ngrok.io",
]
ALLOWED_HOSTS = ["*", "https://e209-83-220-236-197.ngrok.io"]


INSTALLED_APPS = [
    # "dal",
    # "dal_select2",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "shipping",
    "import_export",
    "rangefilter",
    "ajax_select",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "avangard.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        # [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
print(TEMPLATES)
WSGI_APPLICATION = "avangard.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = False
DATE_FORMAT = "d.m.Y"
USE_TZ = True

STATIC_URL = "/static/"

DATE_INPUT_FORMATS = (
    "%d.%m.%Y",
    "%d.%m.%Y",
    "%d.%m.%y",  # '25.10.2006', '25.10.2006', '25.10.06'
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%d/%m/%y",  # '25-10-2006', '25/10/2006', '25/10/06'
    "%d %b %Y",  # '25 Oct 2006',
    "%d %B %Y",  # '25 October 2006',
)
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
