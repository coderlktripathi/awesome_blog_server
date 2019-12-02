from flask import Blueprint, request, make_response, g, current_app as app
from app import blueprint
import bcrypt
from .user import UserResource, UserService
from .common import check_hash


bp = Blueprint('auth', __name__)


@bp.route('/auth/login', methods=['POST'])
def login():
    users = app.data.driver.db['users']
    login_data = request.get_json()
    username = login_data.get('username')
    password = login_data.get('password')
    if not (username or password):
        return make_response({'message': 'Invalid credentials'}, 401)
    
    try:
        user = users.find_one({'username': username})
        if not user:
            return make_response({'message': 'Invalid credentials'}, 401)
 
        if check_hash(password, user.get('password')):
            g.user = user
            return make_response({'message': 'Login success'}, 201)
    except KeyError:
        return make_response({'message': 'Invalid credentials'}, 401)


def init_app(app):
    blueprint(bp, app)

    endpoint_name = 'users'
    service = UserService(endpoint_name)
    UserResource(endpoint_name, app=app, service=service)
