from flask import Blueprint, request, make_response, current_app as app
from app import blueprint
from .user import UserResource, UserService
from .common import check_hash
from .authentication import JwtAuth


bp = Blueprint('auth', __name__)


@bp.route('/auth/login', methods=['POST'])
def login():
    users = app.data.driver.db['users']
    login_data = request.get_json()
    username = login_data.get('username')
    password = login_data.get('password')

    if not (username or password):
        return make_response({'message': 'Invalid credentials'}, 400)

    try:
        user = users.find_one({'username': username})
        if not user:
            return make_response({'message': 'Invalid credentials'}, 400)

        if check_hash(password, user.get('password')):
            token = JwtAuth.generate_token(user['guid'])
            users.update({'username': username}, {"$set": {'token': token}})

            return make_response({'token': token, 'user': JwtAuth.create_response_user(user)}, 201)
    except KeyError:
        return make_response({'message': 'Invalid credentials'}, 400)

    return make_response({'message': 'Invalid credentials'}, 400)


def init_app(app):
    blueprint(bp, app)
    app.auth = JwtAuth()

    endpoint_name = 'users'
    service = UserService(endpoint_name)
    UserResource(endpoint_name, app=app, service=service)
