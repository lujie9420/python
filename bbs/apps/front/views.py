from flask import Blueprint

front_bp = Blueprint("f",__name__,url_prefix='/front')

@front_bp.route('/')
def index():
    return 'front.index'