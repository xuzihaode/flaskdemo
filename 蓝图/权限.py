from flask import Blueprint

bp = Blueprint("权限",__name__, url_prefix="/auth")


@bp.route('login')
def login():
    pass
