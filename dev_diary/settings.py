from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-)yiyzo&h9cf20@xb48v97g87jdz!nj)^n52sf8s$5ib%_k#q9g'

DEBUG = True

ALLOWED_HOSTS = [
    "*",
    ]


INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "ddapp.apps.DdappConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'dev_diary.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dev_diary.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get("DB_USER"),
        'PASSWORD': os.environ.get("DB_PASSWORD"),
        'HOST': os.environ.get("DB_HOST"),
        'PORT': os.environ.get("DB_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "accounts.CustomUser"

SITE_ID = 1 # djangoallauthで利用するdjango.conti¥rib.sitesを使うために必要なサイト識別用のID

AUTHENTICATION_BACKENDS = (
    # 一般ユーザ用メール認証
    "allauth.account.auth_backends.AuthenticationBackend",
    # 管理サイト用メール認証
    "django.contrib.auth.backends.ModelBackend",
)

# メール認証に変更
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False

# サインアップにメールアドレス認証を必要としない
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_REQUIRED = True

# ログインログアウト時の遷移先
LOGIN_REDIRECT_URL = "ddapp:index"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"

# ログアウトのリンククリックで一発ログアウト設定
ACCOUNT_LOGOUT_ON_GET = True

# 認証のメールの件名に自動付与される接頭辞をブランクに
ACCOUNT_EMAIL_SUBJECT_PREFIX = ""

# デフォルトのメール送信元を設定
DEFAULT_FROM_EMAIL = os.environ.get("FROM_EMAIL")

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
