from flask_login import LoginManager
lm = LoginManager()

from flask_mail import Mail
mail = Mail()

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_assets import Environment
assets = Environment()

from flask_babel import Babel
babel = Babel()

from celery import Celery
celery = Celery()
