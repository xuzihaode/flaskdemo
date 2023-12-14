from flask import Blueprint

bp = Blueprint("问答",__name__, url_prefix="/")


@bp.route('/')
def index():
    pass