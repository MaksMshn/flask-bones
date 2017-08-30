class base_config(object):
    """Default configuration options."""
    SITE_NAME = 'Flask Bones'
    SECRET_KEY = b'}B\xec\x01\xabO\x99\x80\x15s\xb2\xb32y\x05\xf8/Y\xf7A\x90\xea\\J'

    SQLALCHEMY_DATABASE_URI = 'postgresql://flask_bones:flask_bones@kast76.utlib.ee:5432/flask_bones'

    SUPPORTED_LOCALES = ['en']


class dev_config(base_config):
    """Development configuration options."""
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_ECHO = True


class test_config(base_config):
    """Testing configuration options."""
    TESTING = True
    WTF_CSRF_ENABLED = False
