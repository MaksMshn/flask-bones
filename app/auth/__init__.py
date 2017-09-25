from flask import Blueprint
import logging

log = logging.getLogger(__name__)

auth = Blueprint('auth', __name__, template_folder='templates')

from . import views
log.info("Loaded auth module")
