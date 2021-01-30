import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

load_dotenv()

SECRET_KEY = os.environ.get('SECRET')

CELERY = {
    'BROKER': os.environ.get('CELERY_BROKER')
}

DATABASE = {
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT'),
    'NAME': os.environ.get('DB_DB_NAME'),
    'USER': os.environ.get('DB_USER'),
    'PASSWORD': os.environ.get('DB_PASS'),
}

AUTH = {
    'ALGORITHM': 'HS256',
    'ACCESS_TOKEN_EXPIRE_MINUTES': 30,
    'SCOPES': {
        'items:read': 'Read items',
        'items:create': 'Create items',
        'items.delete': 'Delete items'
    }
}

POSROCKET = {
    'CLIENT_ID': os.environ.get('POSROCKET_CLIENT_ID'),
    'CLIENT_SECRET': os.environ.get('POSROCKET_CLIENT_SECRET'),
}

OAUTH2_SCHEMA = OAuth2PasswordBearer(tokenUrl='/auth/login', scopes=AUTH['SCOPES'])

