from flask import Blueprint

form_bp = Blueprint('form', __name__, url_prefix='/form')

from . import views