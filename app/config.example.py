class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Flask Bones'
    SECRET_KEY = "very random string"

    SQLALCHEMY_DATABASE_URI = 'postgresql://DB_USER:SET_PASSWORD@localhost:5432/test'

    SUPPORTED_LOCALES = ['en']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'yourGmail@gmail.com'
    MAIL_PASSWORD = 'yourGmail password'


class dev_config(base_config):
    """Development configuration options."""
    FLASK_DEBUG = True
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
