from flask import Blueprint

cal_bp = Blueprint('calendar', __name__, url_prefix='calendar')

from . import views
