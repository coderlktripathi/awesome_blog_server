from flask import Blueprint, request, current_app as app
from app import blueprint
import bcrypt
from .user import UserResource, UserService


bp = Blueprint('auth', __name__)


@bp.route('/auth/login', methods=['POST'])
def login():
    # db = app.data.driver.db['users']
    pass


def init_app(app):
    blueprint(bp, app)

    endpoint_name = 'users'
    service = UserService(endpoint_name)
    UserResource(endpoint_name, app=app, service=service)
