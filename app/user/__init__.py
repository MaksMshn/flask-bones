import logging
from flask import Blueprint

log = logging.getLogger(__name__)

user = Blueprint('user', __name__, template_folder='templates')

from . import views
log.info("Loaded user module")
