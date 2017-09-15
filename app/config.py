import os


class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Flask Bones'
    SECRET_KEY = "very random string"

    # Since I'm using custom config directory for instance specific configs
    # we need to locate it
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_CONFIG_DIR = os.path.join(APP_DIR,"../config")

    #SQLALCHEMY_DATABASE_URI = 'postgresql://ubuntu:ubuntu@localhost:5432/test'
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(APP_DIR, "production.db")

    SUPPORTED_LOCALES = ['en']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'YOUR_GMAIL_ACCOUNT@gmail.com'
    MAIL_PASSWORD = 'YOUR_GMAIL_PASSWORD'

    BROKER_URL = 'redis://localhost:6379'


class dev_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True


class test_config(base_config):
    """Testing configuration options."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    TESTING = True
    WTF_CSRF_ENABLED = False

