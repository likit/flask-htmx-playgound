from flask import Blueprint

table_bp = Blueprint('datatable', __name__, url_prefix='/datatable')

from . import views
