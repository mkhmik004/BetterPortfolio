
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Flask configuration
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True 
WTF_CSRF_ENABLED = True

# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = MAIL_USERNAME

# Set Flask configuration variables
config = {
    'SECRET_KEY': SECRET_KEY,
    'WTF_CSRF_ENABLED': WTF_CSRF_ENABLED,
    'MAIL_SERVER': MAIL_SERVER,
    'MAIL_PORT': MAIL_PORT,
    'MAIL_USE_TLS': MAIL_USE_TLS,
    'MAIL_USE_SSL': MAIL_USE_SSL,
    'MAIL_USERNAME': MAIL_USERNAME,
    'MAIL_PASSWORD': MAIL_PASSWORD,
    'MAIL_DEFAULT_SENDER': MAIL_DEFAULT_SENDER,
}

# Export the config dictionary
__all__ = ['config']
